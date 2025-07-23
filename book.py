from fastapi import FastAPI, Query

app = FastAPI()

books = {
    1: {"title": "Atomic Habits", "author": "James Clear", "in_stock": True},
    2: {"title": "Rich Dad Poor Dad", "author": "Robert Kiyosaki", "in_stock": False},
    3: {"title": "The Alchemist", "author": "Paulo Coelho", "in_stock": True},
}

@app.get("/filter")
def simple_filter(author: str = Query(None), in_stock: bool = Query(None)):
    return {
        book_id: book
        for book_id, book in books.items()
        if (author is None or author.lower() in book["author"].lower())
        and (in_stock is None or book["in_stock"] == in_stock)
    }
