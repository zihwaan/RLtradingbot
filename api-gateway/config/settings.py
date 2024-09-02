from pydantic import BaseSettings

class Settings(BaseSettings):
    API_GATEWAY_PORT: int = 8000
    SECRET_KEY: str = "your-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Service URLs
    DATA_COLLECTOR_URL: str = "http://data-collector:8001"
    DATA_PROCESSOR_URL: str = "http://data-processor:8002"
    MODEL_TRAINER_URL: str = "http://model-trainer:8003"
    INFERENCER_URL: str = "http://inferencer:8004"
    TRADER_URL: str = "http://trader:8005"
    WEB_INTERFACE_URL: str = "http://web-interface:8006"

    # CORS settings
    ALLOWED_ORIGINS: list = ["http://localhost", "http://localhost:3000"]

    # Public paths that don't require authentication
    PUBLIC_PATHS: list = ["/", "/docs", "/redoc", "/openapi.json"]

    class Config:
        env_file = ".env"

settings = Settings()