from app.databases import MotherboardDB
from app.globals import DEFAULT_SKIP, DEFAULT_LIMIT, database, router
from app.models.motherboard_model import MotherBoard, MotherBoardResponse, MotherBoardSearch
from app.routes.standard_router import BaseRouter
from fastapi import Depends

motherboard_api = MotherboardDB(database.motherboard, MotherBoard)
motherboard_route = BaseRouter(motherboard_api)


@router.post("/motherboard/", response_model=MotherBoard, tags=["Motherboard"])
async def post_motherboard(motherboard: MotherBoard):
    return await motherboard_route.post_category(motherboard)


@router.get("/motherboard/all", response_model=MotherBoardResponse, tags=["Motherboard"])
async def get_motherboard(limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    return await motherboard_route.get_category(limit, skip)


@router.get("/motherboard/find/{name:path}", response_model=list[MotherBoard], tags=["Motherboard"])
async def get_motherboard_by_name(name: str):
    return await motherboard_route.get_by_name(name)


@router.get("/motherboard/find", response_model=list[MotherBoard], tags=["Motherboard"])
async def get_motherboard_by_parameters(model: MotherBoardSearch = Depends(), limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    return await motherboard_route.get_by_parameters(model, limit, skip)
