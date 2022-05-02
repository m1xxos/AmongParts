from app.databases import SsdDB
from app.models.ssd_model import SSD, SSDResponse
from app.routes.standard_router import BaseRouter
from app.globals import DEFAULT_SKIP, DEFAULT_LIMIT, database, router

ssd_api = SsdDB(database.ssd, SSD)
ssd_route = BaseRouter(ssd_api)


@router.get("/ssd/all", response_model=SSDResponse, tags=["SSD"])
async def get_ssd(limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    return await ssd_route.get_category(limit, skip)


@router.get("/ssd/find/{name:path}", response_model=list[SSD], tags=["SSD"])
async def get_ssd_by_name(name: str):
    return await ssd_route.get_by_name(name)
