from pydantic import BaseModel, Field

class BookRequest(BaseModel):
    """Request schema for creating a book"""

    book_id: int = Field(gt=0, alias="id")
    title: str = Field(min_length=1, max_length=100)
    author: str = Field(min_length=1, max_length=100)
    category: str = Field(min_length=1, max_length=100)
    rating: int = Field(ge=1, le=5)
