from pydantic import BaseModel, PositiveInt, Field


class TodoRequest(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=3)
    priority: PositiveInt = Field(le=5)
    completed: bool

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Weekly grocery shopping",
                "description": "Remember to buy milk, eggs, and bread",
                "priority": 3,
                "completed": False
            }
        }
