from fastapi import APIRouter

from .endpoints import facebook_router, webhook_router


api_router = APIRouter()

api_router.include_router(facebook_router.router, prefix="/facebook", tags=["Facebook"])
api_router.include_router(webhook_router.router, prefix="/webhook", tags=["Webhook"])
