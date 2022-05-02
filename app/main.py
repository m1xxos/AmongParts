from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import *
from .globals import router
from .user.user_auth import auth_backend
from .user.user_router import fastapi_users

tags_metadata = [
    {"name": "auth", "description": "Авторизация"},
    {"name": "users", "description": "Пользователи"},
    {"name": "Case", "description": "Компьютерные кейсы"},
    {"name": "CPU", "description": "Процессоры"},
    {"name": "Disk Enclosure", "description": "Карманы для накопителей"},
    {"name": "GPU", "description": "Видеокарты"},
    {"name": "HDD", "description": "Жёсткие диски"},
    {"name": "Motherboard", "description": "Материнские платы"},
    {"name": "Optical drive", "description": "Оптические диски"},
    {"name": "Pci controller", "description": "PCI контроллеты"},
    {"name": "PSU", "description": "Блоки питания"},
    {"name": "RAM", "description": "Оперативная память"},
    {"name": "Sound card", "description": "Звуковые карты"},
    {"name": "SSD", "description": "SSD диски"},
    {"name": "Thermo paste", "description": "Термопасты"},
]

app = FastAPI(openapi_tags=tags_metadata)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"Hello": "World"}

app.include_router(router)
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(),
    prefix="/users",
    tags=["users"],
)


