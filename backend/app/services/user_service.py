from fastapi import HTTPException
from app.schemas.user import UserCreate, UserUpdate
from app.crud import user as user_crud
from bcrypt import hashpw, gensalt


# CREATE USER
async def create_user_service(user_data: UserCreate):
    existing_user = await user_crud.get_user_by_email(user_data.email)

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    user_dict = user_data.model_dump()

    # 🔐 HASH PASSWORD (ONLY ONCE, CLEAN WAY)
    user_dict["password"] = hashpw(
    user_dict["password"].encode("utf-8"),
    gensalt()
).decode("utf-8")

    return await user_crud.create_user(user_dict)


# GET USER BY ID
async def get_user_by_id_service(user_id: str):
    user = await user_crud.get_user_by_id(user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


# GET ALL USERS
async def get_all_users_service():
    return await user_crud.get_all_users()


# UPDATE USER
async def update_user_service(user_id: str, update_data: UserUpdate):
    existing_user = await user_crud.get_user_by_id(user_id)

    if not existing_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    update_dict = update_data.dict(exclude_unset=True)

    return await user_crud.update_user(user_id, update_dict)


# DELETE USER
async def delete_user_service(user_id: str):
    existing_user = await user_crud.get_user_by_id(user_id)

    if not existing_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    await user_crud.delete_user(user_id)

    return {"message": "User deleted successfully"}