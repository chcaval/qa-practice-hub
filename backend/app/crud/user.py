from bson import ObjectId
from app.core.database import db
from app.schemas.user import UserUpdate


def user_serializer(user):
    if user is None:
        return None
    user["id"] = str(user["_id"])
    del user["_id"]
    return user

# CREATE USER
async def create_user(user_data: dict):
    result = await db.users.insert_one(user_data)

    user = await db.users.find_one({"_id": result.inserted_id})

    return user_serializer(user)


# GET ALL USERS
async def get_all_users():
    users = []

    async for user in db.users.find():
        users.append(user_serializer(user))

    return users


# GET USER BY ID
async def get_user_by_id(user_id: str):
    user = await db.users.find_one({
        "_id": ObjectId(user_id)
    })

    return user_serializer(user)


# GET USER BY EMAIL
async def get_user_by_email(email: str):
    return await db.users.find_one({
        "email": email
    })

# UPDATE USER
async def update_user(user_id: str, update_data: UserUpdate):
    await db.users.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": update_data.model_dump()}
    )

    user = await db.users.find_one({
        "_id": ObjectId(user_id)
    })

    return user_serializer(user)


# DELETE USER
async def delete_user(user_id: str):
    result = await db.users.delete_one({"_id": ObjectId(user_id)})
    
    return {"deleted": result.deleted_count}