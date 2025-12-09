from fastapi import FastAPI
from app.api.v1 import routes
from app.core.config import settings
from app.db.session import engine, Base

# create DB tables (for simplicity)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Kasparro Backend Assignment")

app.include_router(routes.router, prefix="/api/v1")
