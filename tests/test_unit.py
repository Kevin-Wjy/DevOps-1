# tests/test_unit.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, DevOps!"}


def test_read_item_success():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": "1", "name": "Laptop"}


def test_read_item_not_found():
    response = client.get("/items/999")
    assert response.status_code == 404


def test_create_item_success():
    response = client.post("/items/3?name=Mouse")
    assert response.status_code == 200
    assert response.json() == {"item_id": "3", "name": "Mouse"}


def test_create_item_already_exists():
    response = client.post("/items/1?name=Monitor")
    assert response.status_code == 400
