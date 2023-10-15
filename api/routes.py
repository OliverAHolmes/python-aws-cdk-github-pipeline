from fastapi import APIRouter

router = APIRouter(prefix="/test")


@router.get("/hello")
async def hello():
    return "hello there"
