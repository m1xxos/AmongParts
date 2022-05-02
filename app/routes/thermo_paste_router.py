from app.databases import PasteDB
from app.models.thermo_paste_model import Paste, PasteResponse
from app.routes.standard_router import BaseRouter
from app.globals import DEFAULT_SKIP, DEFAULT_LIMIT, database, router

api = PasteDB(database.paste, Paste)
route = BaseRouter(api)


@router.get("/paste/all", response_model=PasteResponse, tags=["Thermo paste"])
async def get_paste(limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    return await route.get_category(limit, skip)


@router.get("/paste/find/{name:path}", response_model=list[Paste], tags=["Thermo paste"])
async def get_paste_by_name(name: str):
    return await route.get_by_name(name)
