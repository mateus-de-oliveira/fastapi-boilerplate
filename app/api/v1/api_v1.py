from fastapi import APIRouter

from .endpoints import example_router


api_router = APIRouter()

api_router.include_router(example_router.router, prefix="/example", tags=["Example"])
