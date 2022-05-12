from time import monotonic
import motor.motor_asyncio
from bson.objectid import ObjectId
from decouple import config
import os
from dotenv import load_dotenv, find_dotenv
  
load_dotenv(find_dotenv())
MONGO_DETAILS = os.getenv("MONGO_HOST")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.students

user_collection = database.get_collection("user_collection")

# helpers

def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "first_name": user["first_name"],
        "last_name": user["last_name"],
        "email": user["email"],
        "password": user["password"],
    }

# Retrieve all user present in the database
async def retrive_users():
    users = []
    async for user in user_collection.find():
        users.append(user_helper(user))
    return users

# Add user in database
async def add_user(user_data: dict) -> dict:
    user = await user_collection.insert_one(user_data)
    new_user = await user_collection.find_one({"_id": user.inserted_id})
    return user_helper(new_user)

# Retrieve  user present in the database  by user id
async def retrive_user(id: str) -> dict:
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        return user_helper(user)

# Check user already exist or not for validation
async def user_check(email: str) -> dict:
    user = await user_collection.find_one({"email": email})
    if user:
        return user_helper(user)
    return False
    
