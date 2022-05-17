from typing import Optional
import uuid

from fastapi_users import schemas
from pydantic import Field


# TODO Уникальные имена
class UserRead(schemas.BaseUser[uuid.UUID]):
    username: str = Field()
    builds: list = Field()
    liked_builds: list = Field()


class UserCreate(schemas.BaseUserCreate):
    username: str = Field()


class UserUpdate(schemas.BaseUserUpdate):
    username: str = Field()
