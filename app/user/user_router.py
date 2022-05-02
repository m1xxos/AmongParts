from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTStrategy

from app.models.user_model import User, UserCreate, UserUpdate, UserDB
from app.user.user_auth import get_jwt_strategy, auth_backend
from app.user.user_manager import get_user_manager


fastapi_users = FastAPIUsers(
    get_user_manager,
    [auth_backend],
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)
