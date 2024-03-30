from pydantic import BaseModel, EmailStr, Field, validator
import re


class UserRegistration(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8)

    @validator("username")
    def validate_username(cls, value):
        if not re.match("^[a-zA-Z0-9_]+$", value):
            raise ValueError(
                "Username must contain only alphanumeric characters and underscores")
        return value

    @validator("password")
    def validate_password(cls, value):
        if not re.search("[a-z]", value) or not re.search("[A-Z]", value) or not re.search("[0-9]", value):
            raise ValueError(
                "Password must contain at least one uppercase letter, one lowercase letter, and one digit")
        return value
