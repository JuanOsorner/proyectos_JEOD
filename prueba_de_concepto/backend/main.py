from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from compartido.config.base_datos import Base, engine
from funcionalidades.ahe.endpoints import router as ahe_router

# Auto-creación de tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API POC Nómina - Gigha")

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Conectar el router
app.include_router(ahe_router)

@app.get("/")
def health_check():
    return {"estado": "ok", "mensaje": "API de Nómina corriendo correctamente"}