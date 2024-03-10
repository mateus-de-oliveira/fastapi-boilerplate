import logging
from fastapi import APIRouter
from app.schemas.example_schema import ExampleSchema

logger =  logging.getLogger(__name__)

router = APIRouter()

@router.get("/test")
def test():
    logger.error("This is an error message")
    return {"message": "Hello World"}

@router.post("/users", response_model=ExampleSchema)
async def create_user(user: ExampleSchema):

    return user
