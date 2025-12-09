from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_list():
    resp = client.post("/api/v1/records", json={"source_id":"s1","data":"hello"})
    assert resp.status_code == 200
    j = resp.json()
    assert j["source_id"] == "s1"

    resp2 = client.get("/api/v1/records")
    assert resp2.status_code == 200
    assert isinstance(resp2.json(), list)
