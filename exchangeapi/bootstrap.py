from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from exchangeapi.routers.routers import router as api_router

# from pymongo import MongoClient


# def mongoConnect():
#     conn = MongoClient("mongodb://localhost:27017/lab")
#     return conn

# conn = mongoConnect()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.on_event("startup")
# async def create_db_client():
#     # start client here and reuse in future requests

# @app.on_event("shutdown")
# async def shutdown_db_client():
#     # stop your client here

# items = {"foo": "The Foo Wrestlers"}


# @app.get("/")
# def read_root():
#     return {"Hello": "Docker ... Yeah! Its working.... 100 %"}


# @app.get("/items/{item_id}")
# async def read_item(item_id: str):
#     if item_id not in items:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return {"item": items[item_id]}


# @app.get("/items/", tags=["items"])
# async def read_items():
#     return [{"name": "Foo", "price": 42}]


# @app.get("/users/", tags=["users"])
# async def read_users():
#     return [{"username": "johndoe"}]


# @app.get("/elements/", tags=["items"], deprecated=True)
# async def read_elements():
#     return [{"item_id": "Foo"}]


app.include_router(api_router, prefix="/api")
