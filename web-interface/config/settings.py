import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    WEB_INTERFACE_PORT: int = 5000
    KIS_API_URL: str = "https://openapi.koreainvestment.com:9443"
    INITIAL_BALANCE: float = 10000000  # 1천만원

    # KIS API 키 (실제 값은 환경 변수나 .env 파일에서 로드해야 합니다)
    KIS_APP_KEY: str = os.getenv("KIS_APP_KEY", "your_app_key_here")
    KIS_APP_SECRET: str = os.getenv("KIS_APP_SECRET", "your_app_secret_here")

    class Config:
        env_file = ".env"

settings = Settings()