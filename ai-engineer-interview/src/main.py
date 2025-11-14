from fastapi import FastAPI
import os
from database import Database
from utils import save_user_preferences

app = FastAPI(
    title="User Management API",
    description="A FastAPI-based user management service for handling user data and preferences",
    version="1.0.0",
    docs_url="/docs"
)

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")

@app.get("/get/first_route/{user_id}")
def get_user(user_id):
    db = Database()
    user = db.get_user_by_id(user_id)
    if user:
        return user

@app.post("/post/first_route")
def create_user(user_data):
    db = Database()
    new_user = db.create_user(user_data)
    return new_user

@app.put("/put/first_route/{user_id}")
def update_user_preferences(user_id, preferences):
    save_user_preferences(user_id, preferences)
    return {"message": "Preferences saved successfully"}