from fastapi import FastAPI , HTTPException , Path , Query
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

books = {
    1: {"title": "Atomic Habits", "author": "James Clear", "price": 25.99, "in_stock": True},
    2: {"title": "The Subtle Art of Not Giving a F*ck", "author": "Mark Manson", "price": 18.50, "in_stock": False},
    3: {"title": "Rich Dad Poor Dad", "author": "Robert Kiyosaki", "price": 15.75, "in_stock": True},
    4: {"title": "The Alchemist", "author": "Paulo Coelho", "price": 12.99, "in_stock": True},
    5: {"title": "Deep Work", "author": "Cal Newport", "price": 20.00, "in_stock": False}
}
# Define a Pydantic model for the book data
class Book(BaseModel):
    id : int 
    title: str
    author : str
    price :float
    in_stock :bool
    
@app.get("/")
def read_books():
    return books
@app.get("/get-book/{book_id}")
def get_book(book_id:int=Path(... , description="enter the id of the book your looking for ")):
    if book_id not in books :
        raise HTTPException(status_code=404 , details="id not found") 
    return books[book_id]

@app.get("/get-book-by-search")
def search_for_book(
    title: Optional[str] = Query(None, description="search using title"),
    author: Optional[str] = Query(None, description="search using author"),
    price: Optional[float] = Query(None, description="search using price")
):
    results = {
        book_id:books
         for book_id, book in books.items():
        if title and title.lower() in book["title"].lower():
            and
         author and author.lower() in book["author"].lower():
            and
        price and book["price"] == price:
            
    }
   

    if not results:
        raise HTTPException(status_code=404, detail="No book found")
    
    return results



@app.post("/create-book")
def create_book(book:Book , book_id:int):
    if book_id in books:
       raise HTTPException(status_code=400 , details="book already exists")
    books[book_id] = book.dict()
    return books[book_id]
      
@app.put("/update-books/{book_id}")
def update_book(book_id: int, book: Book):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    books[book_id] = book.dict()
    return books[book_id]
@app.delete("/delete-books/{book_id}")
def delete_book(book_id: int):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    delete_book = books.pop(book_id)
    return delete_book