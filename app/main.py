import os
import motor.motor_asyncio
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Depends
from app.databases import *
from fastapi.middleware.cors import CORSMiddleware

from app.routes.standard_router import BaseRouter

tags_metadata = [
    {"name": "Motherboard", "description": "Материнские платы"},
    {"name": "CPU", "description": "Процессоры"},
    {"name": "GPU", "description": "Видеокарты"},
    {"name": "RAM", "description": "Оперативная память"},
    {"name": "PSU", "description": "Блоки питания"},
    {"name": "SSD", "description": "SSD диски"},
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
ssd_api = SsdDB(database.ssd, SSD)

cpu_route = BaseRouter(cpu_api)
motherboard_route = BaseRouter(motherboard_api)
ram_router = BaseRouter(ram_api)
gpu_router = BaseRouter(gpu_api)
psu_router = BaseRouter(psu_api)
ssd_route = BaseRouter(ssd_api)


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


@app.post("/motherboard/", response_model=MotherBoard, tags=["Motherboard"])
async def post_motherboard(motherboard: MotherBoard):
    return await motherboard_route.post_category(motherboard)


@app.get("/motherboard/all", response_model=MotherBoardResponse, tags=["Motherboard"])
async def get_motherboard(limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    return await motherboard_route.get_category(limit, skip)


@app.get("/motherboard/find/{name:path}", response_model=list[MotherBoard], tags=["Motherboard"])
async def get_motherboard_by_name(name: str):
    return await motherboard_route.get_by_name(name)


@app.get("/motherboard/find", response_model=list[MotherBoard], tags=["Motherboard"])
async def get_motherboard_by_parameters(model: MotherBoardSearch = Depends(), limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    return await motherboard_route.get_by_parameters(model, limit, skip)


@app.post("/cpu/", response_model=CPU, tags=["CPU"])
async def post_cpu(cpu: CPU):
    return await cpu_route.post_category(cpu)


@app.get("/cpu/all", response_model=CPUResponse, tags=["CPU"])
async def get_cpu(limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    return await cpu_route.get_category(limit, skip)


@app.get("/cpu/find/{name:path}", response_model=list[CPU], tags=["CPU"])
async def get_cpu_by_name(name: str):
    return await cpu_route.get_by_name(name)


@app.get("/cpu/find", response_model=list[CPU], tags=["CPU"])
async def get_cpu_by_parameters(model: CPUSearch = Depends(), limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    return await cpu_route.get_by_parameters(model, limit, skip)


@app.post("/gpu/", response_model=GPU, tags=["GPU"])
async def post_gpu(gpu: GPU):
    return await gpu_router.post_category(gpu)


@app.get("/gpu/all", response_model=GPUResponse, tags=["GPU"])
async def get_gpu(limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    return await gpu_router.get_category(limit, skip)


@app.get("/gpu/find/{name:path}", response_model=list[GPU], tags=["GPU"])
async def get_gpu_by_name(name: str):
    return await gpu_router.get_by_name(name)


@app.get("/gpu/find", response_model=list[GPU], tags=["GPU"])
async def get_gpu_by_parameters(model: GPUSearch = Depends(), limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    return await gpu_router.get_by_parameters(model, limit, skip)


@app.post("/ram/", response_model=RAM, tags=["RAM"])
async def post_ram(ram: RAM):
    return await ram_router.post_category(ram)


@app.get("/ram/all", response_model=RAMResponse, tags=["RAM"])
async def get_ram(limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    return await ram_router.get_category(limit, skip)


@app.get("/ram/find/{name}", response_model=list[RAM], tags=["RAM"])
async def get_ram_by_name(name: str):
    return await ram_router.get_by_name(name)


@app.get("/ram/find", response_model=list[RAM], tags=["RAM"])
async def get_ram_by_parameters(model: RAMSearch = Depends(), limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    return await ram_router.get_by_parameters(model, limit, skip)


@app.post("/psu/", response_model=PSU, tags=["PSU"])
async def post_psu(psu: PSU):
    return await psu_router.post_category(psu)


@app.get("/psu/all", response_model=PSUResponse, tags=["PSU"])
async def get_psu(limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    return await psu_router.get_category(limit, skip)


@app.get("/psu/find/{name:path}", response_model=list[PSU], tags=["PSU"])
async def get_psu_by_name(name: str):
    return await psu_router.get_by_name(name)


@app.get("/psu/find", response_model=list[PSU], tags=["PSU"])
async def get_psu_by_parameters(model: PSUSearch = Depends(), limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    return await psu_router.get_by_parameters(model, limit, skip)


@app.get("/ssd/all", response_model=SSDResponse, tags=["SSD"])
async def get_ssd(limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    return await ssd_route.get_category(limit, skip)


@app.get("/ssd/find/{name:path}", response_model=list[SSD], tags=["SSD"])
async def get_ssd_by_name(name: str):
    return await ssd_route.get_by_name(name)

# app.include_router(ssd_route.router)
