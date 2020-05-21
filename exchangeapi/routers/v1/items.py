import logging
from fastapi import APIRouter

from exchangeapi.db.mongodb import get_database


router = APIRouter()


@router.get("/v1/users/", tags=["users"])
async def read_users():
    db = get_database()
    collection = db.items
    logging.info("get_database(): {}".format(db))

    records_fetched = collection.find()
    return records_fetched


@router.get("/v1/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser_v1"}


@router.get("/v1/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}
