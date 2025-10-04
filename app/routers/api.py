from fastapi import APIRouter

api_router = APIRouter(prefix="/api", tags=["api"])


@api_router.get("/hello")
async def hello():
    return "Hello, World!"
