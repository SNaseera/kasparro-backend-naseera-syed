"""
Ingest: read data from CSV or Crypto APIs
"""

from typing import List, Dict
import csv
import io
from app.etl.crypto_api import ingest_crypto_data  # new crypto ETL source

def ingest_from_csv_string(csv_text: str) -> List[Dict]:
    """
    Ingest data from a CSV string.
    """
    reader = csv.DictReader(io.StringIO(csv_text))
    return [row for row in reader]

def ingest_all_data(include_crypto: bool = False) -> List[Dict]:
    """
    Combine CSV data and Crypto API data.
    Set include_crypto=True to fetch crypto data as well.
    """
    data: List[Dict] = []

    # Example: ingest CSV (if you have any CSV source)
    SAMPLE_CSV = "id,name\n1,Alice\n2,Bob\n"
    csv_data = ingest_from_csv_string(SAMPLE_CSV)
    data.extend(csv_data)

    # Optional: ingest crypto data
    if include_crypto:
        crypto_data = ingest_crypto_data()
        data.extend(crypto_data)

    return data
