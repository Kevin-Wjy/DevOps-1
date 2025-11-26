# tests/test_integration.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_full_item_flow():
    # Create new item
    create_resp = client.post("/items/10?name=Tablet")
    assert create_resp.status_code == 200
    assert create_resp.json() == {"item_id": "10", "name": "Tablet"}

    # Read the item
    read_resp = client.get("/items/10")
    assert read_resp.status_code == 200
    assert read_resp.json() == {"item_id": "10", "name": "Tablet"}

    # Try to create duplicate
    duplicate_resp = client.post("/items/10?name=Tablet")
    assert duplicate_resp.status_code == 400
