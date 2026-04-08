from dataclasses import dataclass
from decimal import Decimal
from datetime import date

@dataclass
class HoraExtra:
    documento: str
    tipo_hora: str
    cantidad: Decimal
    fecha_reporte: date
    fila_original: str = ""
    numero_linea: int = 0

    def validar(self):
        """
        Aplica las reglas de negocio estrictas.
        Levanta un ValueError si los datos violan las reglas de la empresa.
        """
        if not self.documento or not str(self.documento).strip():
            raise ValueError("El documento del empleado es obligatorio.")

        tipos_validos = ['HE_DIURNA', 'HE_NOCTURNA', 'HE_DOMINICAL', 'HE_FESTIVA']
        if self.tipo_hora not in tipos_validos:
            raise ValueError(f"Tipo de hora '{self.tipo_hora}' no es válido.")

        if self.cantidad <= 0:
            raise ValueError(f"La cantidad de horas debe ser mayor a 0. Recibido: {self.cantidad}")