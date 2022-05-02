from app.databases import GpuDB
from app.models.gpu_model import GPU, GPUResponse, GPUSearch
from app.routes.standard_router import BaseRouter
from app.globals import DEFAULT_SKIP, DEFAULT_LIMIT, database, router
from fastapi import Depends

gpu_api = GpuDB(database.gpu, GPU)
gpu_router = BaseRouter(gpu_api)


@router.post("/gpu/", response_model=GPU, tags=["GPU"])
async def post_gpu(gpu: GPU):
    return await gpu_router.post_category(gpu)


@router.get("/gpu/all", response_model=GPUResponse, tags=["GPU"])
async def get_gpu(limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    return await gpu_router.get_category(limit, skip)


@router.get("/gpu/find/{name:path}", response_model=list[GPU], tags=["GPU"])
async def get_gpu_by_name(name: str):
    return await gpu_router.get_by_name(name)


@router.get("/gpu/find", response_model=list[GPU], tags=["GPU"])
async def get_gpu_by_parameters(model: GPUSearch = Depends(), limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    return await gpu_router.get_by_parameters(model, limit, skip)
