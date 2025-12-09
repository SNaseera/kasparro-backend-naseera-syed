"""
ETL Runner Script
Fetches data from CSV + Crypto APIs, transforms it, and loads into DB
"""

from app.db.session import SessionLocal
from app.etl.ingest import ingest_all_data
from app.etl.transform import transform_record
from app.etl.load import load_records

def main():
    # Ingest data from CSV + Crypto APIs
    rows = ingest_all_data(include_crypto=True)

    # Transform data
    transformed = [transform_record(r) for r in rows]

    # Load data into DB
    db = SessionLocal()
    try:
        load_records(db, transformed)
        print(f"ETL completed successfully. {len(transformed)} records loaded.")
    finally:
        db.close()

if __name__ == "__main__":
    main()
