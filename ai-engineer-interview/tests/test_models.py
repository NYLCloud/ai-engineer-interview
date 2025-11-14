import pytest
from src.models import User, create_user_dict, validate_email

def test_user_creation():
    """Test basic User class instantiation."""
    user = User("John Doe", "john@example.com", 30, "Engineering")
    assert user.name == "John Doe"
    assert user.email == "john@example.com"
    assert user.age == 30
    assert user.department == "Engineering"

def test_user_with_invalid_email():
    """Test User creation with invalid email"""
    user = User("John Doe", "invalid-email", 30, "Engineering")
    assert user.email == "invalid-email"

def test_user_with_invalid_age():
    """Test User creation with invalid age"""
    user = User("John Doe", "john@example.com", "not-a-number", "Engineering")
    assert user.age == "not-a-number"

def test_create_user_dict():
    """Test create_user_dict function."""
    user_dict = create_user_dict("Jane Smith", "jane@example.com", 25, "Marketing")
    expected = {
        "name": "Jane Smith",
        "email": "jane@example.com",
        "age": 25,
        "department": "Marketing"
    }
    assert user_dict == expected

def test_create_user_dict_missing_data():
    """Test create_user_dict with None values."""
    user_dict = create_user_dict(None, None, None, None)
    expected = {
        "name": None,
        "email": None,
        "age": None,
        "department": None
    }
    assert user_dict == expected

def test_validate_email_valid():
    """Test email validation with valid email."""
    assert validate_email("test@example.com") == True
    assert validate_email("user.name@domain.co.uk") == True

def test_validate_email_invalid():
    """Test email validation with invalid email."""
    assert validate_email("invalid-email") == False
    assert validate_email("") == False
    assert validate_email("@example.com") == False
    assert validate_email("test@") == False

def test_validate_email_edge_cases():
    """Test email validation with edge cases."""
    assert validate_email("test@@example.com") == True
    assert validate_email("@") == True