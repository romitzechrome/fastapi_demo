from pickletools import optimize
from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class UsersSchema(BaseModel):
    first_name : str = Field(...)
    last_name : str = Field(...)
    email: EmailStr = Field(...)
    password : str= Field(...)
    
    class Config:
        schema_extra = {
            "example": {
                "first_name": "Lucas anderson",
                "last_name":"anderson",
                "email": "anderson@gmail.com",
                "password": "Lucas@123",
            }
        }


class LoginUserModel(BaseModel):
    email : Optional[EmailStr]
    password :Optional[str]
    class Config:
        schema_extra = {
            "example": {
                "email": "anderson@gmail.com",
                "password": "Lucas@123",
                }
            }