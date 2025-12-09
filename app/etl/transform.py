"""
Transform: clean / normalize records
"""
from typing import Dict

def transform_record(row: Dict[str,str]) -> Dict[str,str]:
    # simple normalization example
    return {
        "source_id": row.get("id") or row.get("source_id") or "unknown",
        "data": str(row)
    }
