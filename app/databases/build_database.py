from fastapi import HTTPException

from app.databases.standard_base import BaseDB
from ..models.builds_model import *
from ..globals import database
from ..user.user_db import User


async def validate_build(build):
    for k, v in build['specifications'].items():
        if v:
            spec = await database[k].find_one({"link_name": v})
            if not spec:
                raise HTTPException(400, f"Элемент {k} не найден")
            del spec["_id"]
            build['specifications'][k] = spec
    return build


def add_image(build):
    if build['specifications']['case']:
        image = build['specifications']['case']['images'][0]
    elif build['specifications']['motherboard']:
        image = build['specifications']['motherboard']['images'][0]
    else:
        image = "https://minio.amongparts.ga/korpusa/default.png"

    return image


class BuildDB(BaseDB):

    async def fetch_all_build(self, build_type, limit, skip):
        builds = []
        search_string = {}
        if build_type:
            search_string = {"type": build_type}

        cursor = self.collection.find(search_string).limit(limit).skip(skip)
        amount = await self.collection.count_documents(search_string)
        async for document in cursor:
            document['specifications'] = [{"key": key, "value": value["name"]} for key, value in
                                          document['specifications'].items() if value]
            builds.append(self.model(**document))
        return amount, builds

    async def create_one(self, build):
        if await self.collection.find_one({'link_name': build['link_name']}):
            raise HTTPException(400, "Сборка с таким названием уже существует")

        document = await validate_build(build)
        build['image'] = add_image(build)
        result = await self.collection.insert_one(document)
        check = await self.collection.find_one({"_id": result.inserted_id}, {"_id": 0})
        return check

    async def fetch_one(self, name):
        document = await self.collection.find_one({"link_name": name}, {"_id": 0})
        if not document:
            raise HTTPException(400, "Сборка с таким названием не существует")

        for specs in document["specifications"]:
            if document["specifications"][specs]:
                document["specifications"][specs]['specifications'] = [{"key": key, "value": value} for key, value in
                                                                       document["specifications"][specs][
                                                                           'specifications'].items()]
        return document

    async def like_build(self, name, user: User):
        build = await self.fetch_one(name)
        if user.username == build['username']:
            raise HTTPException(400, "Эта сборка у вас уже есть")
        for use_build in user.liked_builds:
            if use_build['link_name'] == name:
                raise HTTPException(400, "Эта сборка у вас уже есть")

        build['specifications'] = {key: value["name"] if value else value for key, value in
                                   build['specifications'].items()}
        user_build = build
        return user_build

    async def fetch_user_builds(self, user: User):
        builds = user.builds
        for build in builds:
            build['specifications'] = [{"key": key, "value": value} for key, value in
                                       build['specifications'].items() if value]
        liked_builds = user.liked_builds
        for build in liked_builds:
            build['specifications'] = [{"key": key, "value": value} for key, value in
                                       build['specifications'].items() if value]
        return {"builds": builds, "liked_builds": liked_builds}
