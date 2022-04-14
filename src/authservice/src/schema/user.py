from typing import Optional
from pydantic import BaseModel, EmailStr


class CreateUserSchema(BaseModel):
    first_name: str
    last_name: str
    password: str
    email_id: EmailStr


class UserSchema(BaseModel):
    first_name: str
    last_name: str
    email_id: str
    phone_number: str
    avatar_url: Optional[str]


class LoginSchema(BaseModel):
    email_id: EmailStr
    password: str


class ForgetSchema(BaseModel):
    email_id: EmailStr
    password: str
