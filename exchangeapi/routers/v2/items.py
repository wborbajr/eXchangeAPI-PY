from fastapi import APIRouter

router = APIRouter()


@router.get("/v2/users/", tags=["users"])
async def read_users():
    return [{"username": "Foo_v2"}, {"username": "Bar_v2"}]


@router.get("/v2/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser_v2"}


@router.get("/v2/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}
