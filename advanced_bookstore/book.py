

class Book:

    def __init__(self, book_id: int, title: str, author: str, category: str, rating: int) -> None:
        self.id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.rating = rating

    def __repr__(self) -> str:
        return f"Book(id={self.id}, title={self.title}, author={self.author}, category={self.category}, rating={self.rating})"
