
from fastapi import APIRouter
from src.api.endpoint import authentication

api_router = APIRouter()
api_router.include_router(authentication.router,
                          prefix="/auth", tags=["Authentication"])
