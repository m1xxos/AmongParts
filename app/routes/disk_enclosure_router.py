from app.databases import EnclosureDB
from app.models.disk_enclosure_model import Enclosure, EnclosureResponse
from app.routes.standard_router import BaseRouter
from app.globals import DEFAULT_SKIP, DEFAULT_LIMIT, database, router, DEFAULT_SORT, DEFAULT_DIRECTION

api = EnclosureDB(database.enclosure, Enclosure)
route = BaseRouter(api)


@router.get("/enclosure/all", response_model=EnclosureResponse, tags=["Disk Enclosure"])
async def get_enclosure(limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP, sort: str = DEFAULT_SORT, direction: int = DEFAULT_DIRECTION):
    return await route.get_category(limit, skip, sort, direction)


@router.get("/enclosure/get/{name:path}", response_model=Enclosure, tags=["Disk Enclosure"])
async def get_enclosure_by_name(name: str):
    return await route.get_by_name(name)
