import os
import fastapi
import motor.motor_asyncio
from dotenv import load_dotenv

load_dotenv()
DEFAULT_LIMIT = 10
DEFAULT_SKIP = 0
DEFAULT_SORT = "_id"
DEFAULT_DIRECTION = 1
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"], uuidRepresentation="standard")
database = client.AmongParts
router = fastapi.APIRouter()
