"""
Load: save to DB using CRUD functions
"""
from sqlalchemy.orm import Session
from app import crud, schemas

def load_records(db: Session, records: list[dict]):
    for rec in records:
        payload = schemas.RecordCreate(source_id=rec["source_id"], data=rec["data"])
        crud.create_record(db, payload)
