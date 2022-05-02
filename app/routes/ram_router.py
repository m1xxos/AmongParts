from app.databases import RamDB
from app.models.ram_model import RAM, RAMResponse, RAMSearch
from app.routes.standard_router import BaseRouter
from app.globals import DEFAULT_SKIP, DEFAULT_LIMIT, database, router
from fastapi import Depends

ram_api = RamDB(database.ram, RAM)
ram_router = BaseRouter(ram_api)


@router.post("/ram/", response_model=RAM, tags=["RAM"])
async def post_ram(ram: RAM):
    return await ram_router.post_category(ram)


@router.get("/ram/all", response_model=RAMResponse, tags=["RAM"])
async def get_ram(limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    return await ram_router.get_category(limit, skip)


@router.get("/ram/find/{name}", response_model=list[RAM], tags=["RAM"])
async def get_ram_by_name(name: str):
    return await ram_router.get_by_name(name)


@router.get("/ram/find", response_model=list[RAM], tags=["RAM"])
async def get_ram_by_parameters(model: RAMSearch = Depends(), limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    return await ram_router.get_by_parameters(model, limit, skip)