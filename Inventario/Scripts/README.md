# Scripts y Automatización Python

Este directorio contiene scripts de utilidad y ejercicios algorítmicos desarrollados en Python. Su propósito es automatizar tareas de procesamiento de datos y practicar lógica de programación avanzada.

## Lista de Proyectos

A continuación se describen los componentes principales de este directorio:

1.  **Aplanamiento_datos**:
    -   Herramientas para la manipulación y limpieza de datos.
    -   **`excel.py`**: Script de automatización para procesar archivos de inventario en Excel. Sus funciones incluyen:
        -   Filtrado de registros por responsable.
        -   Indexación y búsqueda de archivos físicos en directorios (recursivo).
        -   Comparación de códigos de inventario con archivos existentes.
        -   Generación de reportes de estado (pendientes/no existen).
    -   **`comando_jd.py`**: Utilidad para sanitizar archivos JSON, eliminando valores sensibles (reemplazándolos por `None`) mientras se preserva la estructura del objeto.

2.  **ejercicios**:
    -   Colección de retos de programación y ejercicios lógicos.
    -   Incluye implementaciones de:
        -   **Decoradores**: Validación de tipos de argumentos.
        -   **Algoritmos**: Búsqueda, recursividad y generación de combinaciones de cadenas.
        -   **Manejo de errores**: Uso de `try/except` y logging.
