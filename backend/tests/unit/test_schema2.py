import pytest
from pydantic import ValidationError
from app.schemas import UserUpdate, UserCreate

def test_create_user_valid():
    user = UserCreate(name="Alice", email="alice@exemplo.com");
    assert user.name == "Alice"
    assert user.email == "alice@exemplo.com"

def  test_create_invalid_email():
    with pytest.raises(ValidationError):
        UserCreate(name="Alice", email="not-a-valid-email")
        
def test_create_missing_name():
    with pytest.raises(ValidationError):
        UserCreate(email="alice@exemplo.com")
        
def test_create_missing_email():
    with pytest.raises(ValidationError):
        UserCreate(name="Alice")
        
def test_user_update_partial():
    update = UserUpdate(name = "Bob")
    assert update.name == "Bob"
    assert update.email is None
    
@pytest.mark.parametrize("email", [
    "bad",
    "missing@",
    "@nodomain.com",
    "spaces in@email.com",
])
    
def test_user_update_reject_invalid_emails(email):
    with pytest.raises(ValidationError):
        UserUpdate(email=email)
    