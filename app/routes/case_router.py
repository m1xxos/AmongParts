from app.databases import CaseDB
from app.models.case_model import Case, CaseResponse
from app.routes.standard_router import BaseRouter
from app.globals import DEFAULT_SKIP, DEFAULT_LIMIT, database, router, DEFAULT_SORT, DEFAULT_DIRECTION

api = CaseDB(database.case, Case)
route = BaseRouter(api)


@router.get("/case/all", response_model=CaseResponse, tags=["Case"])
async def get_case(limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP, sort: str = DEFAULT_SORT, direction: int = DEFAULT_DIRECTION):
    return await route.get_category(limit, skip, sort, direction)


@router.get("/case/get/{name:path}", response_model=Case, tags=["Case"])
async def get_case_by_name(name: str):
    return await route.get_by_name(name)
