import os
import fastapi
import motor.motor_asyncio
from dotenv import load_dotenv

load_dotenv()
DEFAULT_LIMIT = 10
DEFAULT_SKIP = 0
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
database = client.AmongParts
router = fastapi.APIRouter()
