# app/api/v1/__init__.py
from fastapi import APIRouter

# Import the router defined in routes.py
from .routes import router as routes_router

# Create a versioned router for v1 (you can include future v1 sub-routers here)
router = APIRouter()
router.include_router(routes_router, prefix="", tags=["v1"])

# Export for easy import elsewhere
__all__ = ["router"]
