from app.databases import HddDB
from app.models.hdd_model import HDD, HDDResponse
from app.routes.standard_router import BaseRouter
from app.globals import DEFAULT_SKIP, DEFAULT_LIMIT, database, router

api = HddDB(database.hdd, HDD)
route = BaseRouter(api)


@router.get("/hdd/all", response_model=HDDResponse, tags=["HDD"])
async def get_hdd(limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    return await route.get_category(limit, skip)


@router.get("/hdd/find/{name:path}", response_model=list[HDD], tags=["HDD"])
async def get_hdd_by_name(name: str):
    return await route.get_by_name(name)
