from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"title": "One Hundred Years of Solitude", "author": "Gabriel Garcia Marquez", "category": "Novel"},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "category": "Novel"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "category": "Novel"},
    {"title": "Beloved", "author": "Toni Morrison", "category": "Magical Realism"},
    {"title": "Dune", "author": "Frank Herbert", "category": "Science Fiction"},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "category": "Novel"},
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "category": "Fantasy"},
]

@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}


@app.get("/books")
async def read_all_books() -> list[dict[str, str]]:
    return BOOKS


@app.get("/books/{book_title}")
async def read_book(book_title: str) -> dict[str, str]:

    for book in BOOKS:
        if book["title"].lower() == book_title.lower():
            return book
    return {"message": "Book not found"}


@app.get("/books/")
async def filter_books_by_category(category: str) -> list[dict[str, str]]:
    return [book for book in BOOKS if book["category"].lower() == category.lower()]


@app.get("/books/{author}/")
async def filter_books_by_author_and_category(author: str, category: str) -> list[dict[str, str]]:
    return [book for book in BOOKS if book["author"].lower() == author.lower() and book["category"].lower() == category.lower()]
