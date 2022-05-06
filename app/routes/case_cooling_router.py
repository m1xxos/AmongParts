from app.databases import CaseCoolingDB
from app.models.case_cooling_model import CaseCooling, CaseCoolingResponse
from app.routes.standard_router import BaseRouter
from app.globals import DEFAULT_SKIP, DEFAULT_LIMIT, database, router, DEFAULT_SORT, DEFAULT_DIRECTION

api = CaseCoolingDB(database.case_cooling, CaseCooling)
route = BaseRouter(api)


@router.get("/case_cooling/all", response_model=CaseCoolingResponse, tags=["Case Cooling"])
async def get_case(limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP, sort: str = DEFAULT_SORT, direction: int = DEFAULT_DIRECTION):
    return await route.get_category(limit, skip, sort, direction)


@router.get("/case_cooling/get/{name:path}", response_model=CaseCooling, tags=["Case Cooling"])
async def get_case_by_name(name: str):
    return await route.get_by_name(name)
