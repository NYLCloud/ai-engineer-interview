import pytest
from src.database import Database

def test_database_creation():
    """Test Database instantiation."""
    db = Database()
    assert db is not None
    assert len(db.users) == 2
    assert db.users[0]["name"] == "John Doe"
    assert db.users[1]["name"] == "Jane Smith"

def test_get_user_by_id_existing():
    """Test getting existing user by ID."""
    db = Database()
    user = db.get_user_by_id(1)
    assert user is not None
    assert user["name"] == "John"
    assert user["email"] == "doe@example.com"

def test_get_user_by_id_nonexistent():
    """Test getting non-existent user by ID."""
    db = Database()
    user = db.get_user_by_id(999)
    assert user is None

def test_get_user_by_id_wrong_type():
    """Test getting user with wrong ID type - will fail with current implementation."""
    db = Database()
    user = db.get_user_by_id("1")  # String instead of int
    assert user is None  # Will fail because of type mismatch

def test_get_all_users():
    """Test getting all users."""
    db = Database()
    users = db.get_all_users()
    assert len(users) == 2
    assert users[0]["name"] == "John Doe"
    assert users[1]["name"] == "Jane Smith"

def test_create_user_valid():
    """Test creating a new user with valid data."""
    db = Database()
    user_data = {
        "name": "Test User",
        "email": "test@example.com",
        "age": 25
    }
    new_user = db.create_user(user_data)
    assert new_user["id"] == 3
    assert new_user["name"] == "Test User"
    assert new_user["email"] == "test@example.com"
    assert new_user["age"] == 25

def test_create_user_missing_data():
    """Test creating user with missing data - should crash with current implementation."""
    db = Database()
    user_data = {"name": "Incomplete User"}
    # This should fail because email and age keys are missing
    with pytest.raises(KeyError):
        db.create_user(user_data)

def test_create_multiple_users():
    """Test creating multiple users increases ID correctly."""
    db = Database()
    user1_data = {"name": "User1", "email": "user1@test.com", "age": 20}
    user2_data = {"name": "User2", "email": "user2@test.com", "age": 21}
    
    user1 = db.create_user(user1_data)
    user2 = db.create_user(user2_data)
    
    assert user1["id"] == 3
    assert user2["id"] == 4

def test_create_user_empty_database():
    """Test creating user when database is empty - should crash with current implementation."""
    db = Database()
    db.users = []  # Empty the database
    user_data = {"name": "Test", "email": "test@test.com", "age": 25}
    
    # This should fail because max() on empty list raises ValueError
    with pytest.raises(ValueError):
        db.create_user(user_data)

def test_close_connection():
    """Test closing database connection."""
    db = Database()
    db.close_connection()
    assert db.connection is None
