from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ALLOWED_ORIGINS = [
        "https://lajmifundit.eu",
        "https://rea.lajmifundit.eu",
        "http://localhost:5173",
    ]

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
