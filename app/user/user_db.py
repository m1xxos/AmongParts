from typing import Optional

from beanie import PydanticObjectId
from fastapi_users.db import BeanieBaseUser, BeanieUserDatabase
from pydantic import Field


class User(BeanieBaseUser[PydanticObjectId]):
    username: str = Field()
    builds: Optional[list] = Field([])


async def get_user_db():
    yield BeanieUserDatabase(User)
