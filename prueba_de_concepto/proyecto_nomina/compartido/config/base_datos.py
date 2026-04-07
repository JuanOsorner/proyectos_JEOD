import mysql.connector
from mysql.connector import Error

# Configuración centralizada (POC)
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'tu_password',
    'database': 'PruebaNomina'
}

class ConexionDB:
    def __init__(self):
        self.config = DB_CONFIG
        self.conexion = None

    def __enter__(self):
        """Permite usar 'with ConexionDB() as cursor:'"""
        try:
            self.conexion = mysql.connector.connect(**self.config)
            if self.conexion.is_connected():
                return self.conexion
        except Error as e:
            print(f"Error al conectar a MySQL: {e}")
            raise e

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Cierra la conexión automáticamente al salir del bloque 'with'"""
        if self.conexion and self.conexion.is_connected():
            self.conexion.close()