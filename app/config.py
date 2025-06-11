
import os

class Config:
    DB_USER = os.getenv("POSTGRESQL_USER")
    DB_PASS = os.getenv("POSTGRESQL_PASSWORD")
    DB_HOST = os.getenv("POSTGRES_HOST", "postgres")  # Default to Kubernetes service name
    DB_PORT = os.getenv("POSTGRES_PORT", "5432")
    DB_NAME = os.getenv("POSTGRESQL_DATABASE")

    if not all([DB_USER, DB_PASS, DB_NAME]):
        raise ValueError("Missing required DB environment variables!")

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
