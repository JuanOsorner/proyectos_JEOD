from ..Domain.interfaces import LectorDatosInterface, RepositorioNominaInterface
from compartido.bus_eventos.event_bus import bus

class ServicioNomina:
    def __init__(self, lector: LectorDatosInterface, repositorio: RepositorioNominaInterface):
        self.lector = lector
        self.repositorio = repositorio

    def ejecutar(self, fuente_datos) -> dict:
        novedades = self.lector.obtener_datos(fuente_datos)
        
        resultados = {"exitosos": 0, "errores": 0, "detalles_errores": []}

        for item in novedades:
            try:
                item.validar() # Si falla, levanta un ValueError
                self.repositorio.guardar_exitoso(item)
                resultados["exitosos"] += 1
            except Exception as e:
                self.repositorio.guardar_error(item, str(e))
                resultados["errores"] += 1
                resultados["detalles_errores"].append(f"Línea {item.numero_linea}: {str(e)}")

        # Notificamos a cualquier otro módulo que el lote terminó
        bus.publicar("CargaNominaFinalizada", resultados)
        
        return resultados