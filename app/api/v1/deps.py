from typing import Generator
from sqlalchemy.orm import Session
from app.db.session import get_db

# Database dependency for routes
def db_dependency() -> Generator:
    """
    Provides a database session to API routes
    and ensures it is properly closed after use.
    """
    yield from get_db()
