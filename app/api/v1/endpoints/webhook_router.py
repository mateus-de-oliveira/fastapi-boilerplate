from fastapi import APIRouter

router = APIRouter()

@router.get("/leads")
def exemplos():
    return {"leads": "leads"}
