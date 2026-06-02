# Regresión Lineal de Bitcoin con FastAPI

## Descripción

Este proyecto implementa un sistema completo de análisis de datos utilizando Python, FastAPI y JavaScript.

La aplicación consume datos históricos de Bitcoin desde la API pública de CoinGecko, procesa los datos en el backend, calcula una regresión lineal mediante el método de mínimos cuadrados y visualiza los resultados en una interfaz web moderna e interactiva.

El objetivo principal es demostrar la separación de responsabilidades entre capas, el uso de APIs externas, procesamiento de datos y visualización de resultados estadísticos.

---

# Tecnologías Utilizadas

## Backend

* Python 3.x
* FastAPI
* Uvicorn
* NumPy
* Requests

## Frontend

* HTML5
* CSS3
* JavaScript ES6
* Chart.js

## Fuente de Datos

* CoinGecko API

---

# Arquitectura del Proyecto

```text
backend/

├── main.py
├── endpoints/
│   └── regression.py
├── services/
│   └── bitcoin_service.py
├── domain/
│   └── regresion_lineal.py


frontend/

├── views/
│   └── index.html
├── js/
│   ├── api.js
│   ├── app.js
│   └── chart.js
└── css/
    └── styles.css
```

---

# Flujo General

```text
CoinGecko API
        ↓
Bitcoin Service
        ↓
Regresión Lineal
        ↓
Endpoint FastAPI
        ↓
Frontend
        ↓
Visualización
```

---

# Instalación

## Crear entorno virtual

Windows:

```bash
python -m venv venv
```

Activar entorno:

```bash
venv\Scripts\activate
```

---

## Instalar dependencias

```bash
pip install fastapi
pip install uvicorn
pip install numpy
pip install requests
```

o

```bash
pip install -r requirements.txt
```

---

# Ejecución del Backend

Ubicarse dentro de:

```bash
backend
```

Ejecutar:

```bash
uvicorn main:app --reload
```

La API quedará disponible en:

```text
http://127.0.0.1:8000
```

---

# Endpoint Principal

## Obtener regresión lineal de Bitcoin

```http
GET /regression/bitcoin
```

Respuesta:

```json
{
  "data_points": 31,
  "slope": -305.77,
  "intercept": 81757.23,
  "x": [0,1,2,3,...],
  "y": [78654,78520,...],
  "predictions": [81757,81451,...]
}
```

---

# Backend

## main.py

Punto de entrada de FastAPI.

Responsabilidades:

* Crear aplicación FastAPI.
* Configurar CORS.
* Registrar endpoints.

---

## endpoints/regression.py

Responsabilidades:

* Exponer los servicios al cliente.
* Invocar la capa de dominio.
* Retornar resultados serializados.

No contiene lógica matemática.

---

## services/bitcoin_service.py

Responsabilidades:

* Consumir la API de CoinGecko.
* Extraer datos relevantes.
* Transformar la respuesta JSON.
* Generar estructuras utilizables por el dominio.

Salida:

```python
{
    "x": [...],
    "y": [...]
}
```

---

## domain/regresion_lineal.py

Contiene la lógica matemática principal.

Implementa mínimos cuadrados utilizando álgebra lineal.

Modelo:

```text
y = β₀ + β₁x
```

La solución se calcula mediante:

```text
β = (AᵀA)⁻¹Aᵀy
```

donde:

```text
A =
[1 x₁]
[1 x₂]
[1 x₃]
...
```

Retorna:

* Pendiente
* Intercepto
* Predicciones
* Número de muestras

---

# Fundamento Matemático

## Problema

Dados los puntos:

```text
(x₁,y₁)
(x₂,y₂)
...
(xₙ,yₙ)
```

se busca la recta:

```text
y = β₀ + β₁x
```

que minimice:

```text
Σ(yᵢ - ŷᵢ)²
```

---

## Interpretación Geométrica

La regresión lineal proyecta el vector de observaciones sobre el subespacio generado por:

```text
span{1,x}
```

obteniendo la mejor aproximación posible en norma euclídea.

---

# Frontend

## index.html

Contiene:

* Hero principal.
* Resumen.
* Métricas.
* Gráfica.
* Tabla.

Todas las secciones se muestran dinámicamente tras la carga de datos.

---

## api.js

Responsabilidades:

* Comunicación con FastAPI.
* Obtención de datos desde el endpoint.

---

## app.js

Responsabilidades:

* Manejo de eventos.
* Actualización de métricas.
* Actualización de tablas.
* Mensajes de tendencia.
* Animaciones de interfaz.

---

## chart.js

Responsabilidades:

* Construcción del gráfico.
* Configuración de Chart.js.
* Representación de:

  * Datos reales.
  * Recta de regresión.

---

# Experiencia de Usuario

Al iniciar:

* Pantalla centrada.
* Sin scroll.
* Hero principal.

Al cargar datos:

* El Hero se contrae.
* Aparecen las secciones progresivamente.
* Se habilita el scroll.
* Se dibuja la gráfica con animaciones.

---

# Posibles Mejoras

## Matemáticas

* Coeficiente de determinación R².
* Error cuadrático medio (MSE).
* Regresión polinomial.
* Regresión múltiple.
* PCA.
* Descenso de gradiente.

## Backend

* Caché de resultados.
* Manejo avanzado de errores.
* Tests unitarios.

## Frontend

* Dark/Light Mode.
* Exportar CSV.
* Exportar PNG.
* Dashboard multi-activo.

---

# Autor

Juan Esteban Osorno Duque

Proyecto desarrollado como ejercicio de análisis de datos, mínimos cuadrados, arquitectura web y visualización interactiva utilizando Python y FastAPI.
