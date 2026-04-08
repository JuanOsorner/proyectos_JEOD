from sqlalchemy import Column, Integer, String, DateTime, Text, func
from compartido.config.base_datos import Base

class LogErrorNominaDB(Base):
    """Log de errores global (Shared Kernel)"""
    __tablename__ = "Log_Errores_Nomina"

    id_error = Column("IdError", Integer, primary_key=True, autoincrement=True)
    fila_original = Column("FilaOriginal", Text)
    motivo_fallo = Column("MotivoFallo", String(255))
    fecha_fallo = Column("FechaFallo", DateTime, server_default=func.now())