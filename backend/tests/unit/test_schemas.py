import pytest
from pydantic import ValidationError
from app.schemas import UserCreate, UserUpdate


# --- UserCreate validation ---

def test_user_create_valid():
    user = UserCreate(name="Alice", email="alice@example.com")
    assert user.name == "Alice"
    assert user.email == "alice@example.com"


def test_user_create_invalid_email():
    with pytest.raises(ValidationError):
        UserCreate(name="Alice", email="not-an-email")


def test_user_create_missing_name():
    with pytest.raises(ValidationError):
        UserCreate(email="alice@example.com")


def test_user_create_missing_email():
    with pytest.raises(ValidationError):
        UserCreate(name="Alice")


# --- UserUpdate is fully optional ---

def test_user_update_all_fields_optional():
    update = UserUpdate()
    assert update.name is None
    assert update.email is None
    assert update.is_active is None


def test_user_update_partial():
    update = UserUpdate(name="Bob")
    assert update.name == "Bob"
    assert update.email is None


@pytest.mark.parametrize("email", [
    "bad",
    "missing@",
    "@nodomain.com",
    "spaces in@email.com",
])
def test_user_update_rejects_invalid_emails(email):
    with pytest.raises(ValidationError):
        UserUpdate(email=email)
