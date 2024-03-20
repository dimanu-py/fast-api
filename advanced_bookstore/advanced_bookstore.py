from fastapi import FastAPI, Body

from advanced_bookstore.book import Book

app = FastAPI()


books = [
    Book(1, "Python Deep Learning", "Jordi Torres", "Deep Learning", 3),
    Book(2, "Genetic Algorithms with Python", "Daniel Gutierrez", "Genetic Algorithms", 3),
    Book(3, "Clean Code", "Robert C. Martin", "Software Engineering", 4),
    Book(4, "Agile Technical Practices Distilled", "Pedro Moreira Santos", "Test Driven Development", 5),
    Book(5, "The Pragmatic Programmer", "Andrew Hunt", "Software Engineering", 5),
    Book(6, "Head First Design Patterns", "Eric Freeman", "Design Patterns", 5)
]


@app.get("/books")
async def read_all_books():
    return books


@app.post("/books/create_book")
async def create_book(book = Body()) -> dict[str, str]:
    books.append(Book(**book))
    return {"message": "Book has been successfully created"}
