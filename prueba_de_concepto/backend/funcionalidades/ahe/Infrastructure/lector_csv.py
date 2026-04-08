import csv
from typing import List, Any
from ..Domain.reglas_negocio import HoraExtra
from ..Domain.interfaces import LectorDatosInterface
from .mapeadores import HoraExtraMapeador

class LectorCSVMemoria(LectorDatosInterface):
    def obtener_datos(self, contenido_csv: str) -> List[HoraExtra]:
        datos = []
        # Convertimos el string gigante en líneas iterables
        lineas = contenido_csv.splitlines()
        lector = csv.DictReader(lineas)
        
        for i, fila in enumerate(lector, start=2):
            hora_extra = HoraExtraMapeador.desde_diccionario(fila)
            hora_extra.numero_linea = i
            datos.append(hora_extra)
            
        return datos