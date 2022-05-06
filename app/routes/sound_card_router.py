from app.databases import SoundDB
from app.models.sound_card_model import Sound, SoundResponse
from app.routes.standard_router import BaseRouter
from app.globals import DEFAULT_SKIP, DEFAULT_LIMIT, database, router, DEFAULT_SORT, DEFAULT_DIRECTION

api = SoundDB(database.sound, Sound)
route = BaseRouter(api)


@router.get("/sound/all", response_model=SoundResponse, tags=["Sound card"])
async def get_sound(limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP, sort: str = DEFAULT_SORT, direction: int = DEFAULT_DIRECTION):
    return await route.get_category(limit, skip, sort, direction)


@router.get("/sound/get/{name:path}", response_model=Sound, tags=["Sound card"])
async def get_sound_by_name(name: str):
    return await route.get_by_name(name)
