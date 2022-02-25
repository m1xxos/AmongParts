import os
from dotenv import load_dotenv
import motor.motor_asyncio
from models.motherboard_model import *

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


async def fetch_motherboard_by_params(motherboard):
    motherboards = []
    cursor = collection.find(motherboard.dict())
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
