import motor.motor_asyncio

from app.globals import DEFAULT_LIMIT, router

client = motor.motor_asyncio.AsyncIOMotorClient(
    "mongodb+srv://m1xxos:vn9OAsrfRrCEMSmx@amongpartscluster.jbzts.mongodb.net/test?authSource=admin&replicaSet=atlas"
    "-2yea7s-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")
database = client.AmongParts


@router.get("/search", tags=["Search"])
async def search_all(name: str, limit: int = DEFAULT_LIMIT):
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
        {"$limit": limit},
        {
            '$project': {
                '_id': 0
            }
        }
    ]
    cursor = database["summary"].aggregate(pipeline)
    results = []
    async for res in cursor:
        results.append(res)
    return results


@router.get("/search/{category}", tags=["Search"])
async def search_all(category: str, name: str, limit: int = DEFAULT_LIMIT):
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
        }, {"$limit": limit},
        {
            '$project': {
                '_id': 0
            }
        }
    ]
    cursor = database["summary"].aggregate(pipeline)
    results = []
    async for res in cursor:
        results.append(res)
    return results
