from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from app.db.base import Base

class Record(Base):
    __tablename__ = "records"
    id = Column(Integer, primary_key=True, index=True)
    source_id = Column(String, index=True)
    data = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
