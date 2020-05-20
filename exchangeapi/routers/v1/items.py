from fastapi import APIRouter

router = APIRouter()


@router.get("/v1/users/", tags=["users"])
async def read_users():
    return [{"username": "Foo_v1"}, {"username": "Bar_v1"}]


@router.get("/v1/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser_v1"}


@router.get("/v1/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}
