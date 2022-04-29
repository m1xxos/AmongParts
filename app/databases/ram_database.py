from app.models.ram_model import *
from app.databases.standard_base import BaseDB


class RamDB(BaseDB):
    async def fetch_by_params(self, ram, limit, skip):
        rams = []
        search = {}
        if ram.min_price and ram.max_price:
            search["price"] = {'$gte': ram.min_price, '$lte': ram.max_price}
        else:
            if ram.min_price:
                search["price"] = {'$gte': ram.min_price}
            if ram.max_price:
                search["price"] = {'$lte': ram.max_price}
        if ram.type:
            search["type"] = {'$in': ram.type}
        if ram.brand:
            search["brand"] = {'$in': ram.brand}
        if ram.availability:
            search["availability"] = True
        if ram.memory_type:
            search["memory_type"] = {'$in': ram.memory_type}
        if ram.memory_form:
            search["memory_form"] = {'$in': ram.memory_form}
        if ram.memory_speed:
            search["memory_speed"] = {'$in': ram.memory_speed}
        if ram.ecc:
            search["ecc"] = True
        if ram.latency:
            search["latency"] = {'$in': ram.latency}
        if ram.voltage:
            search["voltage"] = {'$in': ram.voltage}
        if ram.memory_module:
            search["memory_module"] = {'$in': ram.memory_module}
        
        cursor = self.collection.find(search).limit(limit).skip(skip)
        async for document in cursor:
            rams.append(RAM(**document))
        return rams
