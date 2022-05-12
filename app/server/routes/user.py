from pydoc import importfile
from tkinter import N
from fastapi import APIRouter, Body,FastAPI, HTTPException, Security
from fastapi.encoders import jsonable_encoder
from ..models.user import UsersSchema,LoginUserModel
from .response  import ResponseModel,ErrorResponseModel
from passlib.context import CryptContext
from ..crud.usercrud import(add_user,retrive_users,user_check)
import requests
from .auth import Auth
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter()
auth_handler = Auth()
security = HTTPBearer()


async def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

async def get_password_hash(password):
    hash_password = pwd_context.hash(password)
    return hash_password


@router.get("/get_user", response_description="User retrieved")
async def get_users(credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    if (auth_handler.decode_token(token)):
        user = await retrive_users()
        if user:
            return ResponseModel(user, "User data retrieved successfully")
        return ResponseModel(user, "Empty list returned")
    else:
        return ErrorResponseModel("An error occurred.", 404, "Token not valid")
    

@router.post("/registration", response_description="user data added into the database")
async def add_user_data(user: UsersSchema = Body(...)):
    user = jsonable_encoder(user)
    passwordd = user["password"]
    email = user["email"]
    check_user = await user_check(email)
    if check_user :
        return ErrorResponseModel("an error occurred",404,"user already exist")
    password = await get_password_hash(passwordd)
    user["password"] = password    
    new_user = await add_user(user)
    return ResponseModel(new_user, "User added successfully.")


@router.post("/login", response_description="user data added into the database")
async def add_user_data(user: LoginUserModel = Body(...)):
    user = jsonable_encoder(user)
    email = user["email"]
    password = user["password"]
    check_user = await user_check(email)
    if check_user :
        hash_password = check_user["password"]
        user_auth = await verify_password(password,hash_password)
        if user_auth:
            access_token = auth_handler.encode_token(check_user["email"])
            refresh_token = auth_handler.encode_refresh_token(check_user["email"])
            data = {'access_token': access_token, 'refresh_token': refresh_token}
            return ResponseModel(data,"Successfully login")
        
        return ErrorResponseModel("an error occurred",404,"Invalide password")
    return ErrorResponseModel("an error occurred",404,"Invalide email")






