from app.models.gpu_model import GPU, GPUSearch
from app.databases.database_base import BaseDB


class GpuDB(BaseDB):
    async def fetch_by_params(self, gpu, limit, skip):
        gpus = []
        search = {}
        if gpu.min_price and gpu.max_price:
            search["price"] = {'$gte': gpu.min_price, '$lte': gpu.max_price}
        else:
            if gpu.min_price:
                search["price"] = {'$gte': gpu.min_price}
            if gpu.max_price:
                search["price"] = {'$lte': gpu.max_price}
        if gpu.type:
            search["type"] = {'$in': gpu.type}
        if gpu.brand:
            search["brand"] = {'$in': gpu.brand}
        if gpu.availability:
            search["availability"] = True
        if gpu.manufacture:
            search["manufacture"] = {'$in': gpu.manufacture}
        if gpu.video_chip:
            search["video_chip"] = {'$in': gpu.video_chip}
        if gpu.video_memory:
            search["video_memory"] = {'$in': gpu.video_memory}
        if gpu.memory_type:
            search["memory_type"] = {'$in': gpu.memory_type}
        if gpu.max_resolution:
            search["max_resolution"] = {'$in': gpu.max_resolution}
        if gpu.ray_tracing:
            search["ray_tracing"] = True
        if gpu.dlss:
            search["dlss"] = True
        if gpu.interface:
            search["interface"] = {'$in': gpu.interface}
        if gpu.power:
            search["power"] = {'$in': gpu.power}
        if gpu.slot_vga:
            search["slot_vga"] = {'$gte': 1}
        if gpu.slot_dvi:
            search["slot_dvi"] = {'$gte': 1}
        if gpu.slot_hdmi:
            search["slot_hdmi"] = {'$gte': 1}
        if gpu.slot_display_port:
            search["slot_display_port"] = {'$gte': 1}
        if gpu.memory_bus:
            search["memory_bus"] = {'$in': gpu.memory_bus}
        if gpu.sli:
            search["sli"] = {'$in': gpu.sli}
        if gpu.min_length and gpu.max_length:
            search["price"] = {'$gte': gpu.min_length, '$lte': gpu.max_length}
        else:
            if gpu.min_length:
                search["price"] = {'$gte': gpu.min_length}
            if gpu.max_length:
                search["price"] = {'$lte': gpu.max_length}

        cursor = self.collection.find(search).limit(limit).skip(skip)
        async for document in cursor:
            gpus.append(GPU(**document))
        return gpus
