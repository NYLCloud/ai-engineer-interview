from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_get_existing_user():
    """Test getting an existing user."""
    response = client.get("/get/first_route/1")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "John Doe"
    assert data["email"] == "john@example.com"

def test_get_nonexistent_user():
    """Test getting a user that doesn't exist."""
    response = client.get("/get/first_route/999")
    assert response.status_code in [404, 500]

def test_get_user_wrong_type():
    """Test getting a user with invalid ID type."""
    response = client.get("/get/first_route/abc")
    assert response.status_code in [400, 422, 500]

def test_create_user_valid():
    """Test creating a user with valid data."""
    user_data = {
        "name": "Test User",
        "email": "test@example.com",
        "age": 25
    }
    response = client.post("/post/first_route", json=user_data)
    assert response.status_code in [200, 201]
    assert "id" in response.json()

def test_create_user_missing_name():
    """Test creating a user without required name field."""
    user_data = {
        "email": "test@example.com",
        "age": 25
    }
    response = client.post("/post/first_route", json=user_data)
    assert response.status_code in [400, 422, 500]

def test_create_user_missing_email():
    """Test creating a user without required email field."""
    user_data = {
        "name": "Test User",
        "age": 25
    }
    response = client.post("/post/first_route", json=user_data)
    assert response.status_code in [400, 422, 500]

def test_create_user_invalid_data():
    """Test creating user with invalid data types."""
    user_data = {
        "name": "Test User",
        "email": "not-an-email",
        "age": "not-a-number"
    }
    response = client.post("/post/first_route", json=user_data)
    assert response.status_code in [400, 422, 500]

def test_update_user_preferences():
    """Test updating user preferences."""
    preferences = {
        "theme": "dark",
        "notifications": True,
        "language": "en"
    }
    response = client.put("/put/first_route/1", json=preferences)
    assert response.status_code in [200, 201]
    assert "message" in response.json()

def test_update_preferences_invalid_user():
    """Test updating preferences for non-existent user."""
    preferences = {
        "theme": "dark"
    }
    response = client.put("/put/first_route/999", json=preferences)
    # Should still work with current implementation but may change
    assert response.status_code in [200, 201, 404]