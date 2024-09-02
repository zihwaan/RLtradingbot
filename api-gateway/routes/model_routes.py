from fastapi import APIRouter, HTTPException
from typing import Dict
import httpx
from config.settings import Settings

router = APIRouter()
settings = Settings()

@router.post("/train")
async def train_model(data: Dict) -> Dict:
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{settings.MODEL_TRAINER_URL}/train", json=data)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to start model training")
    return response.json()

@router.get("/status/{job_id}")
async def get_training_status(job_id: str) -> Dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{settings.MODEL_TRAINER_URL}/status/{job_id}")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to get training status")
    return response.json()