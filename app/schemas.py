from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class RecordCreate(BaseModel):
    source_id: str
    data: str

class RecordRead(RecordCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
