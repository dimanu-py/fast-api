from pydantic import BaseModel, EmailStr, Field


class UserRequest(BaseModel):
    role: str = Field(min_length=3, max_length=100)
    username: str = Field(min_length=3, max_length=100)
    email: EmailStr = Field(min_length=3, max_length=100)
    first_name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
    password: str = Field(min_length=3)

    class Config:
        json_schema_extra = {
            "example": {
                "role": "admin",
                "username": "johndoe",
                "email": "email.example@domain.com",
                "first_name": "John",
                "last_name": "Doe",
                "password": "password123"
            }
        }
