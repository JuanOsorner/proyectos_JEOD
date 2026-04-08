import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Cargamos las variables de entorno
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("La variable DATABASE_URL no está configurada en el archivo .env")

# Creamos el engine con pool de conexiones para escalabilidad
engine = create_engine(
    DATABASE_URL,
    echo=False, 
    pool_pre_ping=True
)

# Fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos de todos los Slices
Base = declarative_base()

def get_db():
    """Generador de sesiones para FastAPI (Dependency Injection)"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()