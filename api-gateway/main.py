from fastapi import FastAPI
from routes import data_routes, model_routes, inference_routes, trade_routes, dashboard_routes
from middlewares import auth_middleware, logging_middleware
from config import settings

app = FastAPI(title="Trading Bot API Gateway")

# Middlewares
app.add_middleware(auth_middleware.AuthMiddleware)
app.add_middleware(logging_middleware.LoggingMiddleware)

# Routes
app.include_router(data_routes.router, prefix="/api/v1/data", tags=["data"])
app.include_router(model_routes.router, prefix="/api/v1/model", tags=["model"])
app.include_router(inference_routes.router, prefix="/api/v1/inference", tags=["inference"])
app.include_router(trade_routes.router, prefix="/api/v1/trade", tags=["trade"])
app.include_router(dashboard_routes.router, prefix="/api/v1/dashboard", tags=["dashboard"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=settings.API_GATEWAY_PORT)