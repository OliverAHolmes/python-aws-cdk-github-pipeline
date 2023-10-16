from fastapi import APIRouter

router = APIRouter(prefix="/test")


@router.get("/")
async def hello():
    return "hello"
