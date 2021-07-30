from typing import Any

from motor.motor_asyncio import AsyncIOMotorClient
from settings import settings
MONGO_DETAILS = settings.db_uri
db_client: AsyncIOMotorClient = None


async def get_db_client() -> AsyncIOMotorClient:
    """Return database client instance."""
    db_client = AsyncIOMotorClient(MONGO_DETAILS)
    return db_client


async def get_collection(name: str = 'forms_collection'):
    db_client = await get_db_client()
    database = db_client.forms
    forms_collection = database.get_collection(name)
    return forms_collection


async def close_db():
    """Close database connection."""
    db_client.close()