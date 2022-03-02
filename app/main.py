import os
import motor.motor_asyncio
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Depends
from app.databases import *
from fastapi.middleware.cors import CORSMiddleware

tags_metadata = [
    {"name": "Motherboard", "description": "Материнские платы"},
    {"name": "CPU", "description": "Процессоры"},
    {"name": "GPU", "description": "Видеокарты"},
    {"name": "RAM", "description": "Оперативная память"},
    {"name": "PSU", "description": "Блоки питания"},
]


load_dotenv()
app = FastAPI(openapi_tags=tags_metadata)
DEFAULT_LIMIT = 10
DEFAULT_SKIP = 0
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
database = client.AmongParts

cpu_api = CpuDB(database.cpu, CPU)
motherboard_api = MotherboardDB(database.motherboard, MotherBoard)
ram_api = RamDB(database.ram, RAM)
gpu_api = GpuDB(database.gpu, GPU)
psu_api = PsuDB(database.psu, PSU)


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


@app.post("/motherboard/", response_model=MotherBoard, tags=["Motherboard"])
async def post_motherboard(motherboard: MotherBoard):
    response = await motherboard_api.create_one(motherboard.dict())
    if response:
        return response
    raise HTTPException(404, "я сломался")


@app.get("/motherboard/all", response_model=list[MotherBoard], tags=["Motherboard"])
async def get_motherboard(limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    response = await motherboard_api.fetch_all(limit, skip)
    return response


@app.get("/motherboard/find/{name}", response_model=list[MotherBoard], tags=["Motherboard"])
async def get_motherboard_by_name(name: str):
    response = await motherboard_api.fetch_one(name)
    if response:
        return response
    raise HTTPException(404, "бро, такого нету")


@app.get("/motherboard/find", response_model=list[MotherBoard], tags=["Motherboard"])
async def get_motherboard_by_parameters(model: MotherBoardSearch = Depends(), limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    response = await motherboard_api.fetch_by_params(model, limit, skip)
    return response


@app.post("/cpu/", response_model=CPU, tags=["CPU"])
async def post_cpu(cpu: CPU):
    response = await cpu_api.create_one(cpu.dict())
    if response:
        return response
    raise HTTPException(404, "я сломался")


@app.get("/cpu/all", response_model=list[CPU], tags=["CPU"])
async def get_cpu(limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    response = await cpu_api.fetch_all(limit, skip)
    return response


@app.get("/cpu/find/{name}", response_model=list[CPU], tags=["CPU"])
async def get_cpu_by_name(name: str):
    response = await cpu_api.fetch_one(name)
    if response:
        return response
    raise HTTPException(404, "бро, такого нету")


@app.get("/cpu/find", response_model=list[CPU], tags=["CPU"])
async def get_cpu_by_parameters(model: CPUSearch = Depends(), limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    response = await cpu_api.fetch_by_params(model, limit, skip)
    return response


@app.post("/gpu/", response_model=GPU, tags=["GPU"])
async def post_gpu(gpu: GPU):
    response = await gpu_api.create_one(gpu.dict())
    if response:
        return response
    raise HTTPException(404, "я сломался")


@app.get("/gpu/all", response_model=list[GPU], tags=["GPU"])
async def get_gpu(limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    response = await gpu_api.fetch_all(limit, skip)
    return response


@app.get("/gpu/find/{name}", response_model=list[GPU], tags=["GPU"])
async def get_gpu_by_name(name: str):
    response = await cpu_api.fetch_one(name)
    if response:
        return response
    raise HTTPException(404, "бро, такого нету")


@app.get("/gpu/find", response_model=list[GPU], tags=["GPU"])
async def get_gpu_by_parameters(model: GPUSearch = Depends(), limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    response = await gpu_api.fetch_by_params(model, limit, skip)
    return response


@app.post("/ram/", response_model=RAM, tags=["RAM"])
async def post_ram(ram: RAM):
    response = await ram_api.create_one(ram.dict())
    if response:
        return response
    raise HTTPException(404, "я сломался")


@app.get("/ram/all", response_model=list[RAM], tags=["RAM"])
async def get_ram(limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    response = await ram_api.fetch_all(limit, skip)
    return response


@app.get("/ram/find/{name}", response_model=list[RAM], tags=["RAM"])
async def get_ram_by_name(name: str):
    response = await ram_api.fetch_one(name)
    if response:
        return response
    raise HTTPException(404, "бро, такого нету")


@app.get("/ram/find", response_model=list[RAM], tags=["RAM"])
async def get_ram_by_parameters(model: RAMSearch = Depends(), limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    response = await ram_api.fetch_by_params(model, limit, skip)
    return response


@app.post("/psu/", response_model=PSU, tags=["PSU"])
async def post_psu(psu: PSU):
    response = await psu_api.create_one(psu.dict())
    if response:
        return response
    raise HTTPException(404, "я сломался")


@app.get("/psu/all", response_model=list[PSU], tags=["PSU"])
async def get_psu(limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    response = await psu_api.fetch_all(limit, skip)
    return response


@app.get("/psu/find/{name}", response_model=list[PSU], tags=["PSU"])
async def get_psu_by_name(name: str):
    response = await psu_api.fetch_one(name)
    if response:
        return response
    raise HTTPException(404, "бро, такого нету")


@app.get("/psu/find", response_model=list[PSU], tags=["PSU"])
async def get_psu_by_parameters(model: PSUSearch = Depends(), limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    response = await psu_api.fetch_by_params(model, limit, skip)
    return response
