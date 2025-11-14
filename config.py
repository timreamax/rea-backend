from pydantic import BaseSettings

class Settings(BaseSettings):
    ALLOWED_ORIGINS = [
        "https://lajmifundit.eu",
        "https://rea.lajmifundit.eu",
        "http://localhost:5173",
    ]

settings = Settings()
