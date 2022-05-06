from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import *
from app.globals import router
from app.user.user_auth import auth_backend
from app.user.user_router import fastapi_users

tags_metadata = [
    {"name": "auth", "description": "Авторизация"},
    {"name": "users", "description": "Пользователи"},
    {"name": "Case Cooling", "description": "Система охлаждения для корпуса"},
    {"name": "Case", "description": "Компьютерные кейсы"},
    {"name": "CPU Cooling", "description": "Система охлаждения для процессора"},
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
    allow_origins=["http://localhost:4200", "https://amongparts.ga"],
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


