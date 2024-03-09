from fastapi import APIRouter

router = APIRouter()

@router.get("/integration")
def integration():
    return {"integration": "facebook"}
