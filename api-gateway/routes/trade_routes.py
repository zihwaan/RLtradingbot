from fastapi import APIRouter, HTTPException
from typing import Dict
import httpx
from config.settings import Settings

router = APIRouter()
settings = Settings()

@router.post("/execute")
async def execute_trade(data: Dict) -> Dict:
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{settings.TRADER_URL}/execute", json=data)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to execute trade")
    return response.json()

@router.get("/status/{order_id}")
async def get_trade_status(order_id: str) -> Dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{settings.TRADER_URL}/status/{order_id}")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to get trade status")
    return response.json()