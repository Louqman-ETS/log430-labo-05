from fastapi import APIRouter
from .products import router as products_router
from .categories import router as categories_router
from .stock import router as stock_router

api_router = APIRouter()

# Include routers
api_router.include_router(products_router, prefix="/products", tags=["products"])
api_router.include_router(categories_router, prefix="/categories", tags=["categories"])
api_router.include_router(stock_router, prefix="/stock", tags=["stock"])
