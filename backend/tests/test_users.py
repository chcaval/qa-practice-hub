from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_user():
    response = client.post("/users/", json={
        "name": "Carlos",
        "email": "test@test.com"
    })

    assert response.status_code == 200 or response.status_code == 201
    data = response.json()

    assert data["name"] == "Carlos"
    assert data["email"] == "test@test.com"