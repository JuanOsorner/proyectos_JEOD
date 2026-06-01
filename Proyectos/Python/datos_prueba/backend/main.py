from fastapi import FastAPI

from endpoints.regression import router as regression_router

app = FastAPI()

app.include_router(regression_router)


@app.get("/")
def home():
    return {
        "status": "ok"
    }