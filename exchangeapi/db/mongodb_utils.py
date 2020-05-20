import logging

from motor.motor_asyncio import AsyncIOMotorClient
from dynaconf import settings

from exchangeapi.db.mongodb import db


async def connect_to_mongo():
    logging.info("Connecting to the database...")

    MONGODB_URL = settings.MONGODB_URL
    MAX_CONNECTIONS_COUNT = settings.MAX_CONNECTIONS_COUNT
    MIN_CONNECTIONS_COUNT = settings.MIN_CONNECTIONS_COUNT

    # logging.info("MONGO URL = {}".format(MONGODB_URL))

    db.client = AsyncIOMotorClient(
        str(MONGODB_URL),
        maxPoolSize=MAX_CONNECTIONS_COUNT,
        minPoolSize=MIN_CONNECTIONS_COUNT,
    )
    logging.info("Successfully connected to the database！")


async def close_mongo_connection():
    logging.info("Closing the database connection...")
    db.client.close()
    logging.info("Database connection closed！")
