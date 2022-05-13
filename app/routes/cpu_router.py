from app.databases import CpuDB
from app.models.cpu_model import CPU, CPUResponse, CPUSearch
from app.routes.standard_router import BaseRouter
from app.globals import DEFAULT_SKIP, DEFAULT_LIMIT, database, router, DEFAULT_SORT, DEFAULT_DIRECTION
from fastapi import Depends

cpu_api = CpuDB(database.cpu, CPU)
cpu_route = BaseRouter(cpu_api)


@router.post("/cpu/", response_model=CPU, tags=["CPU"])
async def post_cpu(cpu: CPU):
    return await cpu_route.post_category(cpu)


@router.get("/cpu/all", response_model=CPUResponse, tags=["CPU"])
async def get_cpu(limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP, sort: str = DEFAULT_SORT, direction: int = DEFAULT_DIRECTION):
    return await cpu_route.get_category(limit, skip, sort, direction)


@router.get("/cpu/get/{name:path}", response_model=CPU, tags=["CPU"])
async def get_cpu_by_name(name: str):
    return await cpu_route.get_by_name(name)


@router.get("/cpu/find", response_model=list[CPU], tags=["CPU"])
async def get_cpu_by_parameters(model: CPUSearch = Depends(), limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    return await cpu_route.get_by_parameters(model, limit, skip)
