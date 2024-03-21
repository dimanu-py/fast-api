from pydantic import BaseModel, Field, PositiveInt


class BookResponse(BaseModel):
    """Response schema for a book"""

    title: str = Field(min_length=1, max_length=100)
    author: str = Field(min_length=1, max_length=100)
    category: str = Field(min_length=1, max_length=100)
    rating: PositiveInt = Field(ge=1, le=5)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Python Object-Oriented Programming",
                "author": "Steven F. Lott",
                "category": "Object-Oriented Programming",
                "rating": 4
            }
        }