from .quotes import router as quotes_router
from fastapi import APIRouter


app_router = APIRouter()


app_router.include_router(quotes_router, prefix="", tags=[""], include_in_schema=False)
