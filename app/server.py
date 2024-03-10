from fastapi import FastAPI
from .api.v1.api_v1 import api_router as api_v1

app = FastAPI()

app.include_router(api_v1, prefix="/api/v1")
