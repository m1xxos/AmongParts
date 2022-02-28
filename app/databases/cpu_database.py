from app.models.cpu_model import CPU, CPUSearch
from app.databases.database_base import BaseDB


class CpuDB(BaseDB):

    async def fetch_by_params(self, cpu, limit, skip):
        cpus = []
        search = {}
        if cpu.min_price and cpu.max_price:
            search["price"] = {'$gte': cpu.min_price, '$lte': cpu.max_price}
        else:
            if cpu.min_price:
                search["price"] = {'$gte': cpu.min_price}
            if cpu.max_price:
                search["price"] = {'$lte': cpu.max_price}
        if cpu.type:
            search["type"] = {'$in': cpu.type}
        if cpu.brand:
            search["brand"] = {'$in': cpu.brand}
        if cpu.series:
            search["series"] = {'$in': cpu.series}
        if cpu.socket:
            search["socket"] = {'$in': cpu.socket}
        if cpu.min_frequency and cpu.max_frequency:
            search["frequency"] = {'$gte': cpu.min_frequency, '$lte': cpu.max_frequency}
        else:
            if cpu.min_frequency:
                search["frequency"] = {'$gte': cpu.min_frequency}
            if cpu.max_frequency:
                search["frequency"] = {'$lte': cpu.max_frequency}
        if cpu.cpu_cores:
            search["socket"] = {'$in': cpu.cpu_cores}
        if cpu.graphics:
            search["graphics"] = True
        if cpu.multiplier:
            search["multiplier"] = True
        if cpu.pci_version:
            search["pci_version"] = {'$in': cpu.pci_version}
        if cpu.tdp:
            search["tdp"] = {'$in': cpu.tdp}

        cursor = self.collection.find(search).limit(limit).skip(skip)
        async for document in cursor:
            cpus.append(CPU(**document))
        return cpus


