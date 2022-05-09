from fastapi import HTTPException

from app.databases.standard_base import BaseDB
from ..models.builds_model import *
from ..globals import database


class BuildDB(BaseDB):

    async def fetch_all_build(self, limit, skip):
        builds = []

        cursor = self.collection.find({}).limit(limit).skip(skip)
        amount = await self.collection.count_documents({})
        async for document in cursor:
            document['specifications'] = [{"key": key, "value": value["name"]} for key, value in
                                          document['specifications'].items() if value]
            builds.append(self.model(**document))
        return amount, builds

    async def create_one(self, build):

        if await self.collection.find_one({'link_name': build['link_name']}):
            raise HTTPException(400, "Сборка с таким названием уже существует")

        document = await self.validate_build(build)
        result = await self.collection.insert_one(document)
        check = await self.collection.find_one({"_id": result.inserted_id})
        del check["_id"]
        return check

    async def validate_build(self, build):
        for k, v in build['specifications'].items():
            if v:
                spec = await database[k].find_one({"link_name": v})
                if not spec:
                    raise HTTPException(400, f"Элемент {k} не найден")
                del spec["_id"]
                build['specifications'][k] = spec
        return build

    async def fetch_one(self, name):
        document = await self.collection.find_one({"link_name": name})
        del document["_id"]
        for specs in document["specifications"]:
            if document["specifications"][specs]:
                document["specifications"][specs]['specifications'] = [{"key": key, "value": value} for key, value in
                                                                       document["specifications"][specs][
                                                                           'specifications'].items()]
        return document
