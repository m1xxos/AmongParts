from app.databases import CpuCoolingDB
from app.models.cpu_cooling_model import CPUCooling, CPUCoolingResponse
from app.routes.standard_router import BaseRouter
from app.globals import DEFAULT_SKIP, DEFAULT_LIMIT, database, router, DEFAULT_SORT, DEFAULT_DIRECTION

api = CpuCoolingDB(database.cpu_cooling, CPUCooling)
route = BaseRouter(api)


@router.get("/cpu_cooling/all", response_model=CPUCoolingResponse, tags=["CPU Cooling"])
async def get_case(limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP, sort: str = DEFAULT_SORT, direction: int = DEFAULT_DIRECTION):
    return await route.get_category(limit, skip, sort, direction)


@router.get("/cpu_cooling/get/{name:path}", response_model=CPUCooling, tags=["CPU Cooling"])
async def get_case_by_name(name: str):
    return await route.get_by_name(name)
