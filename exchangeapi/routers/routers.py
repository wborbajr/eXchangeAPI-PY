from fastapi import APIRouter

from exchangeapi.routers.v1.items import router as items_v1_router
from exchangeapi.routers.v2.items import router as items_v2_router

router = APIRouter()
router.include_router(items_v1_router)
router.include_router(items_v2_router)
