from fastapi import HTTPException
from app.crud import user as user_crud
from app.schemas.auth import LoginRequest
from app.core.security import create_access_token, pwd_context


async def login_service(data: LoginRequest):
    user = await user_crud.get_user_by_email(data.email)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    try:
        password_ok = pwd_context.verify(data.password, user["password"])
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not password_ok:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user["email"]})

    return {
        "access_token": token,
        "token_type": "bearer"
    }