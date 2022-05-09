from fastapi import HTTPException, Depends, Query
from slugify import slugify
from app.databases import BuildDB
from app.models.builds_model import Build, BuildResponse, BuildPost
from app.globals import DEFAULT_SKIP, DEFAULT_LIMIT, database, router
from app.user.user_db import User
from app.user.user_router import current_active_user

api = BuildDB(database["build"], Build)


@router.post("/build/", response_model=BuildPost, tags=["Build"])
async def post_build(build: BuildPost, user: User = Depends(current_active_user)):
    build = build.dict()
    build['username'] = user.username
    build['link_name'] = slugify(build['name'])
    response = await api.create_one(build)
    if response:
        user.builds.append(response)
        await user.save()
        return response
    raise HTTPException(404, "Произошла ошибка")


@router.get("/build/all", response_model=BuildResponse, tags=["Build"])
async def get_build(limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    response_amount, response = await api.fetch_all_build(limit, skip)
    return {"amount": response_amount, "data": response}


@router.get("/build/get/{name:path}", response_model=Build, tags=["Build"])
async def get_build_by_name(name: str):
    response = (await api.fetch_one(name))
    if response:
        return response
    raise HTTPException(404, "Ничего не найдено")
