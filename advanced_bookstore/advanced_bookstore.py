from typing import Any

from fastapi import FastAPI, Path, Query, HTTPException

from advanced_bookstore.book import Book
from advanced_bookstore.request_schema import BookRequest
from advanced_bookstore.response_schema import BookResponse

app = FastAPI()


books = [
    Book(1, "Python Deep Learning", "Jordi Torres", "Deep Learning", 3),
    Book(2, "Genetic Algorithms with Python", "Daniel Gutierrez", "Genetic Algorithms", 3),
    Book(3, "Clean Code", "Robert C. Martin", "Software Engineering", 4),
    Book(4, "Agile Technical Practices Distilled", "Pedro Moreira Santos", "Test Driven Development", 5),
    Book(5, "The Pragmatic Programmer", "Andrew Hunt", "Software Engineering", 5),
    Book(6, "Head First Design Patterns", "Eric Freeman", "Design Patterns", 5)
]


@app.get("/books", response_model=list[BookResponse])
async def read_all_books() -> Any:
    return books


@app.get("/books/{book_id}", response_model=BookResponse)
async def read_book(book_id: int = Path(gt=0)) -> Any:
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail=f"Book with id {book_id} not found")


@app.get("/books/publish/", response_model=list[BookResponse])
async def filter_books_by_published_date(published_date: str = Query(..., description="When the book was published")) -> Any:
    filtered_books = [book for book in books if str(book.published_date) == published_date]
    return filtered_books


@app.post("/books/create_book")
async def create_book(book: BookRequest) -> dict[str, str]:
    new_book = Book(**book.model_dump())
    books.append(generate_book_id(new_book))
    return {"message": "Book has been successfully created"}


@app.put("/books/update_book")
async def update_book(book: BookRequest) -> dict[str, str]:
    for idx, book_to_update in enumerate(books):
        if book_to_update.id == book.book_id:
            book_to_update = Book(**book.model_dump())
            books[idx] = book_to_update
            return {"message": "Book has been successfully updated"}
    raise HTTPException(status_code=404, detail=f"Book with id {book.book_id} not found")


@app.delete("/books/delete/{book_id}")
async def delete_book(book_id: int = Path(gt=0)) -> dict[str, str]:
    for book in books:
        if book.id == book_id:
            books.remove(book)
            return {"message": "Book has been successfully deleted"}
    raise HTTPException(status_code=404, detail=f"Book with id {book_id} not found")


def generate_book_id(book: Book) -> Book:
    book.id = len(books) + 1
    return book
