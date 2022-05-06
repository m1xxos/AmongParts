from app.databases import HddDB
from app.models.hdd_model import HDD, HDDResponse
from app.routes.standard_router import BaseRouter
from app.globals import DEFAULT_SKIP, DEFAULT_LIMIT, database, router, DEFAULT_SORT, DEFAULT_DIRECTION

api = HddDB(database.hdd, HDD)
route = BaseRouter(api)


@router.get("/hdd/all", response_model=HDDResponse, tags=["HDD"])
async def get_hdd(limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP, sort: str = DEFAULT_SORT, direction: int = DEFAULT_DIRECTION):
    return await route.get_category(limit, skip, sort, direction)


@router.get("/hdd/get/{name:path}", response_model=HDD, tags=["HDD"])
async def get_hdd_by_name(name: str):
    return await route.get_by_name(name)
