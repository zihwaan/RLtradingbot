from fastapi import APIRouter, HTTPException, Depends
from typing import Dict
import httpx
from config.settings import Settings

router = APIRouter()
settings = Settings()

@router.get("/market")
async def get_market_data() -> Dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{settings.DATA_COLLECTOR_URL}/collect/market")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch market data")
    return response.json()

@router.post("/collect")
async def collect_data(data: Dict) -> Dict:
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{settings.DATA_COLLECTOR_URL}/collect/historical", json=data)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to start data collection")
    return response.json()

@router.post("/process")
async def process_data(data: Dict) -> Dict:
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{settings.DATA_PROCESSOR_URL}/process", json=data)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to process data")
    return response.json()