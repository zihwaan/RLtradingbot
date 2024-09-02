from fastapi import APIRouter, HTTPException
from typing import Dict
import httpx
from config.settings import Settings

router = APIRouter()
settings = Settings()

@router.get("/performance")
async def get_performance() -> Dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{settings.WEB_INTERFACE_URL}/api/performance")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to get performance data")
    return response.json()

@router.get("/settings")
async def get_settings() -> Dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{settings.WEB_INTERFACE_URL}/api/settings")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to get settings")
    return response.json()

@router.put("/settings")
async def update_settings(data: Dict) -> Dict:
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{settings.WEB_INTERFACE_URL}/api/settings", json=data)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to update settings")
    return response.json()

@router.get("/logs")
async def get_logs() -> Dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{settings.WEB_INTERFACE_URL}/api/logs")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to get logs")
    return response.json()