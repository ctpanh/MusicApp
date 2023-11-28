from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Login(BaseModel):
    email: str
    password: str


class RegisterUser(Login):
    user_name: str

    class Config:
        orm_mode = True


class ConfirmPassword(BaseModel):
    currentPass: str


class UpdateUser(ConfirmPassword):
    email: Optional[str] = None
    newPassword: Optional[str] = None
    user_name: Optional[str] = None
