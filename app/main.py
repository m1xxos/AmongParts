from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.globals import router


tags_metadata = [
    {"name": "Motherboard", "description": "Материнские платы"},
    {"name": "CPU", "description": "Процессоры"},
    {"name": "GPU", "description": "Видеокарты"},
    {"name": "RAM", "description": "Оперативная память"},
    {"name": "PSU", "description": "Блоки питания"},
    {"name": "SSD", "description": "SSD диски"},
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

