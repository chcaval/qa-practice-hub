from fastapi import APIRouter

from .routes.users import router as users_router
from .routes.ai import router as ai_router
from .routes.auth import router as auth_router

api_router = APIRouter()

api_router.include_router(users_router)
api_router.include_router(ai_router)
api_router.include_router(auth_router)