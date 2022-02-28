import os
from dotenv import load_dotenv
import motor.motor_asyncio
from app.models.cpu_model import *

load_dotenv()

client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
database = client.AmongParts
collection = database.cpu


async def create_cpu(cpu):
    document = cpu
    result = await collection.insert_one(document)
    return document


async def fetch_all_cpus(limit, skip):
    cpus = []
    cursor = collection.find({}).limit(limit).skip(skip)
    async for document in cursor:
        cpus.append(CPU(**document))
    return cpus


async def fetch_one_cpu(name):
    cpus = []
    find_string = {"name": name}
    cursor = collection.find(find_string)
    async for document in cursor:
        cpus.append(CPU(**document))
    return cpus


async def fetch_cpu_by_params(cpu, limit, skip):
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

    print(search)
    cursor = collection.find(search).limit(limit).skip(skip)
    async for document in cursor:
        cpus.append(CPU(**document))
    return cpus
