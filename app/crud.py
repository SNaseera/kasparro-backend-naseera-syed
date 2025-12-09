from sqlalchemy.orm import Session
from app import models, schemas

def create_record(db: Session, record_in: schemas.RecordCreate):
    db_obj = models.Record(source_id=record_in.source_id, data=record_in.data)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_records(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Record).offset(skip).limit(limit).all()
