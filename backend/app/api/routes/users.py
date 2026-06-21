from fastapi import APIRouter, status
from ...core.security import get_current_user
from fastapi import Depends


from ...schemas.user import (
    UserCreate,
    UserUpdate,
    UserResponse
)

from ...services.user_service import (
    create_user_service,
    get_all_users_service,
    get_user_by_id_service,
    update_user_service,
    delete_user_service
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

    
# CREATE USER
@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_user(payload: UserCreate):
    return await create_user_service(payload)


# LIST USERS
@router.get("/", response_model=list[UserResponse])
async def list_users(user=Depends(get_current_user)):
    return await get_all_users_service()


@router.get("/me")
async def get_me(user=Depends(get_current_user)):
    return user


# GET USER BY ID
@router.get("/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: str,
    user = Depends(get_current_user)
):
    return await get_user_by_id_service(user_id)


# UPDATE USER
@router.put("/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: str,
    payload: UserUpdate
):
    return await update_user_service(
        user_id,
        payload
    )


# DELETE USER
@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_user(user_id: str):
    await delete_user_service(user_id)
