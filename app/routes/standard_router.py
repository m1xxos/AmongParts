from fastapi import HTTPException

from app.databases import BaseDB


class BaseRouter:
    def __init__(self, api: BaseDB):
        self.api = api

    async def get_category(self, limit, skip, sort, direction):
        response_amount, response = await self.api.fetch_all(limit, skip, sort, direction)
        return {"amount": response_amount, "data": response}

    async def get_by_name(self, name):
        response = (await self.api.fetch_one(name))
        if response:
            return response
        raise HTTPException(404, "Ничего не найдено")

    async def get_by_parameters(self, model, limit, skip):
        response = await self.api.fetch_by_params(model, limit, skip)
        if response:
            return response
        raise HTTPException(404, "Ничего не найдено")

    async def post_category(self, category):
        response = await self.api.create_one(category.dict())
        if response:
            return response
        raise HTTPException(404, "Произошла ошибка")



