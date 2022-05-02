from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import *
from .globals import router

tags_metadata = [
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

