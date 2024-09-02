from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import data_routes, model_routes, inference_routes, trade_routes, dashboard_routes
from middlewares.auth_middleware import AuthMiddleware
from middlewares.logging_middleware import LoggingMiddleware
from config.settings import Settings

settings = Settings()

app = FastAPI(title="Trading Bot API Gateway")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Custom middlewares
app.add_middleware(AuthMiddleware)
app.add_middleware(LoggingMiddleware)

# Routes
app.include_router(data_routes.router, prefix="/api/v1/data", tags=["data"])
app.include_router(model_routes.router, prefix="/api/v1/model", tags=["model"])
app.include_router(inference_routes.router, prefix="/api/v1/inference", tags=["inference"])
app.include_router(trade_routes.router, prefix="/api/v1/trade", tags=["trade"])
app.include_router(dashboard_routes.router, prefix="/api/v1/dashboard", tags=["dashboard"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Trading Bot API Gateway"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=settings.API_GATEWAY_PORT)