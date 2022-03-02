from app.models.psu_model import PSU, PSUSearch
from app.databases.database_base import BaseDB


class PsuDB(BaseDB):
    async def fetch_by_params(self, psu, limit, skip):
        psus = []
        search = {}
        if psu.min_price and psu.max_price:
            search["price"] = {'$gte': psu.min_price, '$lte': psu.max_price}
        else:
            if psu.min_price:
                search["price"] = {'$gte': psu.min_price}
            if psu.max_price:
                search["price"] = {'$lte': psu.max_price}
        if psu.type:
            search["type"] = {'$in': psu.type}
        if psu.brand:
            search["brand"] = {'$in': psu.brand}
        if psu.detach_cables:
            search["detach_cables"] = True
        if psu.braided_cables:
            search["braided_cables"] = True
        if psu.min_wattage and psu.max_wattage:
            search["wattage"] = {'$gte': psu.min_wattage, '$lte': psu.max_wattage}
        else:
            if psu.min_wattage:
                search["wattage"] = {'$gte': psu.min_wattage}
            if psu.max_wattage:
                search["wattage"] = {'$lte': psu.max_wattage}
        if psu.power_cpu_motherboard:
            search["power_cpu_motherboard"] = {'$in': psu.power_cpu_motherboard}
        if psu.efficiency_standard:
            search["efficiency_standard"] = {'$in': psu.efficiency_standard}
        if psu.fan_size:
            search["fan_size"] = {'$in': psu.fan_size}
        if psu.form_factor:
            search["form_factor"] = {'$in': psu.form_factor}
        if psu.power_gpu:
            search["power_gpu"] = {'$in': psu.power_gpu}

        cursor = self.collection.find(search).limit(limit).skip(skip)
        async for document in cursor:
            psus.append(PSU(**document))
        return psus
