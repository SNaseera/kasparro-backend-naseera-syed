from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app import schemas, crud

router = APIRouter()

@router.post("/records", response_model=schemas.RecordRead)
def create_record(record: schemas.RecordCreate, db: Session = Depends(get_db)):
    return crud.create_record(db, record)

@router.get("/records", response_model=list[schemas.RecordRead])
def list_records(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_records(db, skip, limit)
