from app.databases import OpticalDB
from app.models.optical_drive_model import Optical, OpticalResponse
from app.routes.standard_router import BaseRouter
from app.globals import DEFAULT_SKIP, DEFAULT_LIMIT, database, router, DEFAULT_SORT, DEFAULT_DIRECTION

api = OpticalDB(database.optical, Optical)
route = BaseRouter(api)


@router.get("/optical/all", response_model=OpticalResponse, tags=["Optical drive"])
async def get_optical(limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP, sort: str = DEFAULT_SORT, direction: int = DEFAULT_DIRECTION):
    return await route.get_category(limit, skip, sort, direction)


@router.get("/optical/get/{name:path}", response_model=Optical, tags=["Optical drive"])
async def get_optical_by_name(name: str):
    return await route.get_by_name(name)
