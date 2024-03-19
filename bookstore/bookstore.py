from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"title": "One Hundred Years of Solitude", "author": "Gabriel Garcia Marquez", "category": "Novel"},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "category": "Novel"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "category": "Novel"},
    {"title": "Beloved", "author": "Toni Morrison", "category": "Magical Realism"},
    {"title": "Dune", "author": "Frank Herbert", "category": "Science Fiction"},
]

@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}