from pydantic import BaseModel, EmailStr


# ----------------------
# USER BASE
# ----------------------
class UserBase(BaseModel):
    name: str
    email: EmailStr


# ----------------------
# CREATE USER (POST)
# ----------------------
class UserCreate(UserBase):
    pass


# ----------------------
# UPDATE USER (PUT/PATCH)
# ----------------------
class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    is_active: bool | None = None


# ----------------------
# RESPONSE MODEL
# ----------------------
class UserResponse(BaseModel):
    id: str   # IMPORTANT: MongoDB uses string ObjectId
    name: str
    email: str
    is_active: bool

    model_config = {"from_attributes": True}


# ----------------------
# AI REQUEST
# ----------------------
class SummarizeRequest(BaseModel):
    text: str


# ----------------------
# AI RESPONSE
# ----------------------
class SummarizeResponse(BaseModel):
    summary: str
    word_count: int
    model: str