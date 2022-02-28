import os
import motor.motor_asyncio
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Depends
from app.databases.motherboard_database import *
from app.databases.cpu_database import *
from fastapi.middleware.cors import CORSMiddleware


load_dotenv()
app = FastAPI()
DEFAULT_LIMIT = 10
DEFAULT_SKIP = 0
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
database = client.AmongParts

cpu_api = CpuDB(database.cpu, CPU)
motherboard_api = MotherboardDB(database.motherboard, MotherBoard)


origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/motherboard/", response_model=MotherBoard)
async def post_motherboard(motherboard: MotherBoard):
    response = await motherboard_api.create_one(motherboard.dict())
    if response:
        return response
    raise HTTPException(404, "я сломался")


@app.get("/motherboard/all", response_model=list[MotherBoard])
async def get_motherboard(limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    response = await motherboard_api.fetch_all(limit, skip)
    return response


@app.get("/motherboard/find/{name}", response_model=list[MotherBoard])
async def get_motherboard_by_name(name: str):
    response = await motherboard_api.fetch_one(name)
    if response:
        return response
    raise HTTPException(404, "бро, такого нету")


@app.get("/motherboard/find", response_model=list[MotherBoard])
async def get_motherboard_by_parameters(model: MotherBoardSearch = Depends(), limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    response = await motherboard_api.fetch_by_params(model, limit, skip)
    return response


@app.post("/cpu/", response_model=CPU)
async def post_cpu(cpu: CPU):
    response = await cpu_api.create_one(cpu.dict())
    if response:
        return response
    raise HTTPException(404, "я сломался")


@app.get("/cpu/all", response_model=list[CPU])
async def get_cpu(limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    response = await cpu_api.fetch_all(limit, skip)
    return response


@app.get("/cpu/find/{name}", response_model=list[CPU])
async def get_cpu_by_name(name: str):
    response = await cpu_api.fetch_one(name)
    if response:
        return response
    raise HTTPException(404, "бро, такого нету")


@app.get("/cpu/find", response_model=list[CPU])
async def get_cpu_by_parameters(model: CPUSearch = Depends(), limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    response = await cpu_api.fetch_by_params(model, limit, skip)
    return response
