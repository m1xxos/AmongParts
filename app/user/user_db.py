import motor.motor_asyncio
from fastapi_users.db import MongoDBUserDatabase
from app.globals import client
from app.models.user_model import UserDB


db = client["AmongUsers"]
collection = db["users"]


async def get_user_db():
    yield MongoDBUserDatabase(UserDB, collection)
