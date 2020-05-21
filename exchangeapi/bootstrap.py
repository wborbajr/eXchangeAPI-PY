from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from exchangeapi.routers.routers import router as api_router
from exchangeapi.db.mongodb_utils import connect_to_mongo, close_mongo_connection


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)

app.include_router(api_router, prefix="/api")
