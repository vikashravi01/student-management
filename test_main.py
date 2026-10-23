from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_student():
    r = client.post("/students", json={"name": "Test User", "age": 21})
    assert r.status_code == 201
    data = r.json()
    assert data["name"] == "Test User"
    assert "id" in data
    client.delete(f"/students/{data['id']}")  # clean up


def test_get_student_not_found():
    r = client.get("/students/999999")
    assert r.status_code == 404


def test_invalid_data_returns_422():
    r = client.post("/students", json={"name": "", "age": 500})
    assert r.status_code == 422


def test_update_and_delete_student():
    sid = client.post("/students", json={"name": "Temp", "age": 20}).json()["id"]

    r = client.put(f"/students/{sid}", json={"name": "Updated", "age": 22})
    assert r.status_code == 200
    assert r.json()["name"] == "Updated"

    assert client.delete(f"/students/{sid}").status_code == 200
    assert client.get(f"/students/{sid}").status_code == 404