from sqlalchemy.orm import Session
from ..Domain.interfaces import RepositorioNominaInterface
from ..Domain.reglas_negocio import HoraExtra

# El modelo privado de este Slice
from .persistence.models import NovedadHoraExtraDB
# El modelo global (Shared Kernel)
from compartido.infraestructura.modelos_comunes import LogErrorNominaDB

class RepositorioSQL(RepositorioNominaInterface):
    def __init__(self, db_session: Session):
        # Inyectamos la sesión para no abrir y cerrar conexiones a lo loco
        self.db = db_session

    def guardar_exitoso(self, hora_extra: HoraExtra):
        nueva_novedad = NovedadHoraExtraDB(
            documento=hora_extra.documento,
            tipo_hora=hora_extra.tipo_hora,
            cantidad=hora_extra.cantidad,
            fecha_reporte=hora_extra.fecha_reporte
        )
        self.db.add(nueva_novedad)
        # Nota: Haremos el commit() en la capa de aplicación para transaccionalidad en bloque

    def guardar_error(self, hora_extra: HoraExtra, motivo: str):
        motivo_con_fila = f"Línea {hora_extra.numero_linea}: {motivo}"
        nuevo_error = LogErrorNominaDB(
            fila_original=hora_extra.fila_original,
            motivo_fallo=motivo_con_fila
        )
        self.db.add(nuevo_error)