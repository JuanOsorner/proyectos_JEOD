from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from compartido.config.base_datos import get_db

# Al estar en la raíz de 'ahe', usamos un solo punto para acceder a las carpetas
from .Application.servicio_limpieza import ServicioNomina
from .Infrastructure.lector_csv import LectorCSVMemoria
from .Infrastructure.repositorio_sql import RepositorioSQL

router = APIRouter(prefix="/api/ahe", tags=["Análisis Horas Extras"])

@router.post("/cargar-csv")
async def cargar_csv(archivo: UploadFile = File(...), db: Session = Depends(get_db)):
    if not archivo.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Formato inválido. Debe ser un archivo CSV.")
    
    contenido_bytes = await archivo.read()
    try:
        contenido_str = contenido_bytes.decode('utf-8-sig') 
    except UnicodeDecodeError:
        raise HTTPException(status_code=400, detail="Error de codificación. Asegúrate de usar UTF-8.")

    lector = LectorCSVMemoria()
    repo = RepositorioSQL(db)
    servicio = ServicioNomina(lector, repo)
    
    try:
        resumen = servicio.ejecutar(contenido_str)
        db.commit() 
        return {"mensaje": "Procesamiento completado", "resumen": resumen}
    except Exception as e:
        db.rollback() 
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")