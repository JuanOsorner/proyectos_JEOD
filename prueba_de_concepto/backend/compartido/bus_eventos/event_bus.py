from typing import Callable, Dict, List, Any

class SimpleEventBus:
    def __init__(self):
        # Diccionario donde la llave es el nombre del evento 
        # y el valor es una lista de funciones a ejecutar.
        self._subscribers: Dict[str, List[Callable]] = {}

    def suscribir(self, evento_nombre: str, callback: Callable):
        """Registra una función para que se ejecute cuando ocurra el evento."""
        if evento_nombre not in self._subscribers:
            self._subscribers[evento_nombre] = []
        self._subscribers[evento_nombre].append(callback)

    def publicar(self, evento_nombre: str, data: Any = None):
        """Dispara el evento y ejecuta todas las funciones suscritas."""
        if evento_nombre in self._subscribers:
            for callback in self._subscribers[evento_nombre]:
                callback(data)

# Instancia única (Singleton) para ser compartida en toda la app
bus = SimpleEventBus()