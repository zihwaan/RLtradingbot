from fastapi import APIRouter, HTTPException
from typing import Dict
import httpx
from config.settings import Settings

router = APIRouter()
settings = Settings()

@router.post("/predict")
async def predict(data: Dict) -> Dict:
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{settings.INFERENCER_URL}/predict", json=data)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to get prediction")
    return response.json()