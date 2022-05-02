from app.databases import PsuDB
from app.models.psu_model import PSU, PSUResponse, PSUSearch
from app.routes.standard_router import BaseRouter
from app.globals import DEFAULT_SKIP, DEFAULT_LIMIT, database, router
from fastapi import Depends

psu_api = PsuDB(database.psu, PSU)
psu_router = BaseRouter(psu_api)


@router.post("/psu/", response_model=PSU, tags=["PSU"])
async def post_psu(psu: PSU):
    return await psu_router.post_category(psu)


@router.get("/psu/all", response_model=PSUResponse, tags=["PSU"])
async def get_psu(limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    return await psu_router.get_category(limit, skip)


@router.get("/psu/find/{name:path}", response_model=list[PSU], tags=["PSU"])
async def get_psu_by_name(name: str):
    return await psu_router.get_by_name(name)


@router.get("/psu/find", response_model=list[PSU], tags=["PSU"])
async def get_psu_by_parameters(model: PSUSearch = Depends(), limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    return await psu_router.get_by_parameters(model, limit, skip)