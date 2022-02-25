from fastapi import FastAPI, HTTPException
from databases.motherboard_database import *
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/motherboard/", response_model=MotherBoard)
async def post_motherboard(motherboard: MotherBoard):
    response = await create_motherboard(motherboard.dict())
    if response:
        return response
    raise HTTPException(400, "я сломался")


@app.get("/motherboard/all", response_model=list[MotherBoard])
async def get_motherboard(limit: int = 10, skip: int = 0, ):
    response = await fetch_all_motherboards(limit, skip)
    return response


@app.get("/motherboard/find/{name}", response_model=list[MotherBoard])
async def get_motherboard_by_name(name: str):
    response = await fetch_one_motherboard(name)
    if response:
        return response
    raise HTTPException(404, "бро, такого нету")


@app.get("/motherboard/find",)
async def get_motherboard_by_parameters(motherboard: MotherBoardSearch):
    response = await fetch_motherboard_by_params(motherboard)
    return response


# @app.get("/api/todo")
# async def get_todo():
#     response = await fetch_all_todos()
#     return response
#
#
# @app.get("/api/todo/{title}", response_model=Todo)
# async def get_todo_by_title(title):
#     response = await fetch_one_todo(title)
#     if response:
#         return response
#     raise HTTPException(404, f"There is no todo with the title {title}")
#
#
# @app.post("/api/todo/", response_model=Todo)
# async def post_todo(todo: Todo):
#     response = await create_todo(todo.dict())
#     if response:
#         return response
#     raise HTTPException(400, "Something went wrong")
#
#
# @app.put("/api/todo/{title}/", response_model=Todo)
# async def put_todo(title: str, desc: str):
#     response = await update_todo(title, desc)
#     if response:
#         return response
#     raise HTTPException(404, f"There is no todo with the title {title}")
#
#
# @app.delete("/api/todo/{title}")
# async def delete_todo(title):
#     response = await remove_todo(title)
#     if response:
#         return "Successfully deleted todo"
#     raise HTTPException(404, f"There is no todo with the title {title}")