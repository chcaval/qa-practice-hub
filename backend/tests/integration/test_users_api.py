import pytest


# --- Health check ---

def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


# --- Create user ---

def test_create_user_success(client):
    response = client.post("/users", json={"name": "Alice", "email": "alice@example.com"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Alice"
    assert data["email"] == "alice@example.com"
    assert data["is_active"] is True
    assert "id" in data


def test_create_user_duplicate_email_returns_409(client):
    client.post("/users", json={"name": "Alice", "email": "alice@example.com"})
    response = client.post("/users", json={"name": "Alice2", "email": "alice@example.com"})
    assert response.status_code == 409


def test_create_user_invalid_email_returns_422(client):
    response = client.post("/users", json={"name": "Alice", "email": "bad-email"})
    assert response.status_code == 422


def test_create_user_missing_fields_returns_422(client):
    response = client.post("/users", json={"name": "Alice"})
    assert response.status_code == 422


# --- Get user ---

def test_get_user_success(client):
    created = client.post("/users", json={"name": "Bob", "email": "bob@example.com"}).json()
    response = client.get(f"/users/{created['id']}")
    assert response.status_code == 200
    assert response.json()["email"] == "bob@example.com"


def test_get_user_not_found_returns_404(client):
    response = client.get("/users/9999")
    assert response.status_code == 404


# --- List users ---

def test_list_users_empty(client):
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == []


def test_list_users_returns_all(client):
    client.post("/users", json={"name": "Alice", "email": "alice@example.com"})
    client.post("/users", json={"name": "Bob", "email": "bob@example.com"})
    response = client.get("/users")
    assert len(response.json()) == 2


# --- Update user ---

def test_update_user_name(client):
    created = client.post("/users", json={"name": "Old Name", "email": "user@example.com"}).json()
    response = client.put(f"/users/{created['id']}", json={"name": "New Name"})
    assert response.status_code == 200
    assert response.json()["name"] == "New Name"


def test_update_user_not_found_returns_404(client):
    response = client.put("/users/9999", json={"name": "X"})
    assert response.status_code == 404


def test_deactivate_user(client):
    created = client.post("/users", json={"name": "Alice", "email": "alice@example.com"}).json()
    response = client.put(f"/users/{created['id']}", json={"is_active": False})
    assert response.json()["is_active"] is False


# --- Delete user ---

def test_delete_user_success(client):
    created = client.post("/users", json={"name": "Alice", "email": "alice@example.com"}).json()
    response = client.delete(f"/users/{created['id']}")
    assert response.status_code == 204


def test_delete_user_not_found_returns_404(client):
    response = client.delete("/users/9999")
    assert response.status_code == 404


def test_deleted_user_no_longer_retrievable(client):
    created = client.post("/users", json={"name": "Alice", "email": "alice@example.com"}).json()
    client.delete(f"/users/{created['id']}")
    response = client.get(f"/users/{created['id']}")
    assert response.status_code == 404
