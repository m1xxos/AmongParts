from fastapi import HTTPException, Depends, Query, Body
from slugify import slugify
from app.databases import BuildDB
from app.models.builds_model import Build, BuildResponse, BuildPost
from app.globals import DEFAULT_SKIP, DEFAULT_LIMIT, database, router
from app.user.user_db import User
from app.user.user_router import current_active_user

api = BuildDB(database["build"], Build)


@router.post("/build/", tags=["Build"])
async def post_build(build: BuildPost = Body(...), user: User = Depends(current_active_user)):
    build = build.dict()
    build['username'] = user.username
    if not build["name"]:
        raise HTTPException(400, "Необходимо указать название сборки")
    build['link_name'] = slugify(build['name'])
    response = await api.create_one(build)
    if response:
        build = response
        build['specifications'] = {key: value["name"] if value else value for key, value in
                                   build['specifications'].items()}
        user.builds.append(build)
        await user.save()
        return response
    raise HTTPException(404, "Произошла ошибка")


@router.post('/build/like/', tags=["Build"])
async def like_build(name: str, user: User = Depends(current_active_user)):
    result = await api.like_build(name, user)
    user.liked_builds.append(result)
    await user.save()
    return result


@router.get("/build/all", response_model=BuildResponse, tags=["Build"])
async def get_build(build_type: str = None, limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    response_amount, response = await api.fetch_all_build(build_type, limit, skip)
    return {"amount": response_amount, "data": response}


@router.get("/build/get/{name:path}", tags=["Build"])
async def get_build_by_name(name: str):
    response = await api.fetch_one(name)
    if response:
        return response
    raise HTTPException(404, "Ничего не найдено")


@router.get("/users/builds", tags=["users"])
async def get_users_builds(user: User = Depends(current_active_user)):
    result = await api.fetch_user_builds(user)
    return result
