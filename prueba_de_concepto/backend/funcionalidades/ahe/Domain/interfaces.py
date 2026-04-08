from abc import ABC, abstractmethod
from typing import List, Any
from .reglas_negocio import HoraExtra

class LectorDatosInterface(ABC):
    @abstractmethod
    def obtener_datos(self, fuente: Any) -> List[HoraExtra]:
        """Extrae los datos y los convierte en entidades de Dominio"""
        pass

class RepositorioNominaInterface(ABC):
    @abstractmethod
    def guardar_exitoso(self, hora_extra: HoraExtra):
        """Guarda la entidad válida en la base de datos transaccional"""
        pass

    @abstractmethod
    def guardar_error(self, hora_extra: HoraExtra, motivo: str):
        """Guarda el registro fallido en el log de auditoría"""
        pass