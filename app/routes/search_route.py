import motor.motor_asyncio

from app.globals import DEFAULT_LIMIT, router, DEFAULT_SKIP

client = motor.motor_asyncio.AsyncIOMotorClient(
    "mongodb+srv://m1xxos:vn9OAsrfRrCEMSmx@amongpartscluster.jbzts.mongodb.net/test?authSource=admin&replicaSet=atlas"
    "-2yea7s-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")
database = client.AmongParts


@router.get("/search", tags=["Search"])
async def search_all(name: str, limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    pipeline = [
        {
            "$search": {
                "index": "summary_search",
                "text": {
                    "query": name,
                    "path": "name"
                }
            }
        },
        {"$skip": skip},
        {"$limit": limit},
        {
            '$project': {
                '_id': 0
            }
        }
    ]
    pipeline_count = [
        {
            '$search': {
                'index': 'summary_search',
                'text': {
                    'query': name,
                    'path': 'name'
                }
            }
        },
        {
            '$count': 'amount'
        }
    ]

    cursor = database["summary"].aggregate(pipeline)
    results = []
    async for res in cursor:
        results.append(res)

    cursor = database["summary"].aggregate(pipeline_count)
    amount = await cursor.to_list(1)
    if amount:
        amount = amount[0]['amount']
    else:
        amount = 0

    return {"amount": amount, "data": results}


@router.get("/search/{category}", tags=["Search"])
async def search_all(category: str, name: str, limit: int = DEFAULT_LIMIT, skip: int = DEFAULT_SKIP):
    pipeline = [
        {
            '$search': {
                'index': 'summary_search',
                'text': {
                    'query': name,
                    'path': 'name'
                }
            }
        }, {
            '$match': {
                'category': category
            }
        }, {"$skip": skip},
        {"$limit": limit},
        {
            '$project': {
                '_id': 0
            }
        }
    ]
    pipeline_count = [
        {
            '$search': {
                'index': 'summary_search',
                'text': {
                    'query': name,
                    'path': 'name'
                }
            }
        },{
            '$match': {
                'category': category
            }
        },
        {
            '$count': 'amount'
        }
    ]
    cursor = database["summary"].aggregate(pipeline)
    results = []
    async for res in cursor:
        results.append(res)

    cursor = database["summary"].aggregate(pipeline_count)
    amount = await cursor.to_list(1)
    if amount:
        amount = amount[0]['amount']
    else:
        amount = 0
    return {"amount": amount, "data": results}
