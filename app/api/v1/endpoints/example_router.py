import logging
from fastapi import APIRouter

logger =  logging.getLogger(__name__)

router = APIRouter()

@router.get("/test")
def test():
    logger.error("This is an error message")
    return {"message": "Hello World"}
