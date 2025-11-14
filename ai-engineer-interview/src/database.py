import os
from typing import Optional, List, Dict, Any

class Database:
    """Database service for user management operations."""
    
    def __init__(self):
        print("Initializing database connection...")

        self.database_url = os.getenv("DATABASE_URL")
        print(f"Connecting to: {self.database_url}")

        self._connection = self._connect()
        self._setup_test_data()
        print("Database service ready!")
    
    def _connect(self):
        """Simulate database connection setup."""
        # In a real app, this would be something like:
        # return create_engine(self.database_url)
        return {"status": "connected", "url": self.database_url}
    
    def _setup_test_data(self):
        """Initialize with some test data for development."""
        self._users_table = [
            {"id": 1, "name": "John Doe", "email": "john@example.com", "age": 30},
            {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "age": 25},
        ]
        self._user_preferences_table = {}
    
    def execute_query(self, query: str) -> Any:
        """Execute a raw SQL query against the database."""
        print(f"Executing query: {query}")
        return {"rows_affected": 1, "status": "success"}
    
    def get_user_by_id(self, user_id: int) -> Optional[Dict[str, Any]]:
        """Fetch user by ID from database."""
        self.execute_query(f"SELECT * FROM users WHERE id = {user_id}")
        for user in self._users_table:
            if user["id"] == user_id:
                return user
        return None
    
    def get_user_by_email(self, email: str) -> Optional[Dict[str, Any]]:
        """Fetch user by email from database."""
        self.execute_query(f"SELECT * FROM users WHERE email = '{email}'")
        for user in self._users_table:
            if user["email"] == email:
                return user
        return None
    
    def get_all_users(self) -> List[Dict[str, Any]]:
        """Fetch all users from database."""
        self.execute_query("SELECT * FROM users")
        return self._users_table.copy()
    
    def create_user(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """Insert new user into database."""
        self.execute_query("INSERT INTO users (name, email, age) VALUES (...)")
        
        # Generate new ID
        max_id = max([user["id"] for user in self._users_table]) if self._users_table else 0
        new_user = {
            "id": max_id + 1,
            "name": user_data["name"],
            "email": user_data["email"],
            "age": user_data["age"]
        }
        
        self._users_table.append(new_user)

        print(f"User created with ID: {new_user['id']}")
        return new_user
    
    def update_user(self, user_id: int, user_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Update existing user in database."""
        self.execute_query(f"UPDATE users SET ... WHERE id = {user_id}")
        for i, user in enumerate(self._users_table):
            if user["id"] == user_id:
                self._users_table[i].update(user_data)
                return self._users_table[i]
        return None
    
    def delete_user(self, user_id: int) -> bool:
        """Delete user from database."""
        self.execute_query(f"DELETE FROM users WHERE id = {user_id}")
        for i, user in enumerate(self._users_table):
            if user["id"] == user_id:
                del self._users_table[i]
                return True
        return False
    
    def save_user_preferences(self, user_id: int, preferences: Dict[str, Any]) -> bool:
        """Save user preferences to database."""
        self.execute_query(f"INSERT/UPDATE user_preferences WHERE user_id = {user_id}")
        self._user_preferences_table[user_id] = preferences
        return True
    
    def get_user_preferences(self, user_id: int) -> Optional[Dict[str, Any]]:
        """Get user preferences from database."""
        self.execute_query(f"SELECT * FROM user_preferences WHERE user_id = {user_id}")
        return self._user_preferences_table.get(user_id)
    
    def close(self):
        """Close database connection."""
        print("Closing database connection...")
        self._connection = None
