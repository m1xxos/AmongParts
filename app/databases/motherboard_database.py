import os
from dotenv import load_dotenv
import motor.motor_asyncio
from app.models.motherboard_model import *

load_dotenv()

client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
database = client.AmongParts
collection = database.motherboard


async def create_motherboard(motherboard):
    document = motherboard
    result = await collection.insert_one(document)
    return document


async def fetch_all_motherboards(limit, skip):
    motherboards = []
    cursor = collection.find({}).limit(limit).skip(skip)
    async for document in cursor:
        motherboards.append(MotherBoard(**document))
    return motherboards


async def fetch_one_motherboard(name):
    motherboards = []
    find_string = {"name": name}
    cursor = collection.find(find_string)
    async for document in cursor:
        motherboards.append(MotherBoard(**document))
    return motherboards


async def fetch_motherboard_by_params(motherboard, limit, skip):
    motherboards = []
    search = {}
    if motherboard.min_price and motherboard.max_price:
        search["price"] = {'$gte': motherboard.min_price, '$lte': motherboard.max_price}
    else:
        if motherboard.min_price:
            search["price"] = {'$gte': motherboard.min_price}
        if motherboard.max_price:
            search["price"] = {'$lte': motherboard.max_price}
    if motherboard.type:
        search["type"] = {'$in': motherboard.type}
    if motherboard.brand:
        search["brand"] = {'$in': motherboard.brand}
    if motherboard.socket:
        search["socket"] = {'$in': motherboard.socket}
    if motherboard.memory_slots:
        search["memory_slots"] = {'$in': motherboard.memory_slots}
    if motherboard.chipset:
        search["chipset"] = {'$in': motherboard.chipset}
    if motherboard.form_factor:
        search["form_factor"] = {'$in': motherboard.form_factor}
    if motherboard.pci_2:
        search["pci_2"] = {'$gte': 1}
    if motherboard.pci_3:
        search["pci_3"] = {'$gte': 1}
    if motherboard.pci_4:
        search["pci_4"] = {'$gte': 1}
    if motherboard.pci_5:
        search["pci_5"] = {'$gte': 1}
    if motherboard.raid:
        search["raid"] = {'raid': True}
    if motherboard.optane:
        search["optane"] = {'optane': True}
    if motherboard.wi_fi:
        search["wi_fi"] = {'wi_fi': True}
    if motherboard.bluetooth:
        search["bluetooth"] = {'bluetooth': True}
    if motherboard.memory_type:
        search["memory_type"] = {'$in': motherboard.memory_type}
    if motherboard.sata:
        search["sata_amount"] = {'$gte': 1}
    if motherboard.m_2:
        search["m_2_amount"] = {'$gte': 1}
    if motherboard.sli:
        search["sli"] += {'$in': motherboard.sli}

    cursor = collection.find(search).limit(limit).skip(skip)
    async for document in cursor:
        motherboards.append(MotherBoard(**document))
    return motherboards


# async def fetch_one_todo(title):
#     document = await collection.find_one({"title": title})
#     return document
#
#
# async def fetch_all_todos():
#     todos = []
#     cursor = collection.find({})
#     async for document in cursor:
#         todos.append(Todo(**document))
#     return todos
#
#
# async def create_todo(todo):
#     document = todo
#     result = await collection.insert_one(document)
#     return document
#
#
# async def update_todo(title, desc):
#     await collection.update_one({"title": title}, {"$set": {"description": desc}})
#     document = await collection.find_one({"title": title})
#     return document
#
#
# async def remove_todo(title):
#     await collection.delete_one({"title": title})
#     return True
