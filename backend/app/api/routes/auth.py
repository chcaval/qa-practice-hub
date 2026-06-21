from fastapi import APIRouter

from app.schemas.auth import LoginRequest
from app.services.auth_service import login_service
from app.schemas.auth import LoginRequest, LoginResponse

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/login", response_model=LoginResponse)
async def login(payload: LoginRequest):
    return await login_service(payload)


