from fastapi import APIRouter

from app.api.endpoints import (
    webhook_router,
)

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(webhook_router, prefix="/webhook", tags=["webhook"])
