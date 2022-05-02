import motor.motor_asyncio
from fastapi_users.db import MongoDBUserDatabase
from ..globals import client
from ..models.user_model import UserDB


db = client["AmongUsers"]
collection = db["users"]


async def get_user_db():
    yield MongoDBUserDatabase(UserDB, collection)
