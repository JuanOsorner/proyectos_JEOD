from fastapi import FastAPI
# Añadimos los middlewares aqui para evitar bloqueos (Aqui lo dejamos por cuestiones educativas)
from fastapi.middleware.cors import CORSMiddleware

from endpoints.regression import router as regression_router

app = FastAPI()

# Aqui dejamos la configuración de nuestro middleware, todo lo dejamos por defecto
# Evitamos que las urls del front y el back esten en distintos puertos
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(regression_router)


@app.get("/")
def home():
    return {
        "status": "ok"
    }