from datetime import date
from typing import Optional

from pydantic import BaseModel, Field, PositiveInt


class BookRequest(BaseModel):
    """Request schema for creating a book"""

    book_id: Optional[PositiveInt] = Field(alias="id", default=None)
    title: str = Field(min_length=1, max_length=100)
    author: str = Field(min_length=1, max_length=100)
    category: str = Field(min_length=1, max_length=100)
    rating: int = Field(ge=1, le=5)
    published_date: date

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Python Object-Oriented Programming",
                "author": "Steven F. Lott",
                "category": "Object-Oriented Programming",
                "rating": 4,
                "published_date": "2021-06-01"
            }
        }
