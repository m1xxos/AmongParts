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
            document['specifications'] = [{"key": key, "value": value} for key, value in
                                          document['specifications'].items()]
            builds.append(self.model(**document))
        return amount, builds

    async def fetch_all_info(self):
        pass

    async def create_one(self, build):
        document = build
        print(build['link_name'])

        if await self.collection.find_one({'link_name': build['link_name']}):
            raise HTTPException(404, "Сборка с таким названием уже существует")

        result = await self.collection.insert_one(document)
        check = await self.collection.find_one({"_id": result.inserted_id})
        del check["_id"]
        return check
