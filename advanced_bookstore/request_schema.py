from typing import Optional

from pydantic import BaseModel, Field, PositiveInt


class BookRequest(BaseModel):
    """Request schema for creating a book"""

    book_id: Optional[PositiveInt] = Field(alias="id", default=None)
    title: str = Field(min_length=1, max_length=100)
    author: str = Field(min_length=1, max_length=100)
    category: str = Field(min_length=1, max_length=100)
    rating: int = Field(ge=1, le=5)
