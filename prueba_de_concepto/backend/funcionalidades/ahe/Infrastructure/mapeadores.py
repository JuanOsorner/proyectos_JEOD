from decimal import Decimal, InvalidOperation
from datetime import datetime, date
from ..Domain.reglas_negocio import HoraExtra

class HoraExtraMapeador:
    @staticmethod
    def desde_diccionario(datos: dict) -> HoraExtra:
        # 1. Limpieza preventiva (Data Scrubbing)
        documento = str(datos.get('documento', '')).strip()
        tipo_hora = str(datos.get('tipo_he', '')).strip().upper()
        
        # 2. Manejo de tipos sucios (ej: "cinco" -> falla, " 5.5 " -> 5.5)
        try:
            cantidad_str = str(datos.get('cantidad_horas', '0')).strip()
            cantidad = Decimal(cantidad_str) 
        except InvalidOperation:
            cantidad = Decimal('-1') # Forzamos fallo en el dominio
            
        # 3. Manejo de fechas
        try:
            fecha_str = str(datos.get('fecha_reporte', '')).strip()
            fecha_dt = datetime.strptime(fecha_str, '%Y-%m-%d').date()
        except ValueError:
            fecha_dt = date.today() # Podrías manejarlo distinto, pero forzamos un valor por defecto

        return HoraExtra(
            documento=documento,
            tipo_hora=tipo_hora,
            cantidad=cantidad,
            fecha_reporte=fecha_dt,
            fila_original=str(datos)
        )