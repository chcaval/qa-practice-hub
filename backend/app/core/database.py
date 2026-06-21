from motor.motor_asyncio import AsyncIOMotorClient
from app.core.security import pwd_context
MONGO_URL = "mongodb://localhost:27017"

client = AsyncIOMotorClient(MONGO_URL)

db = client.qa_practice