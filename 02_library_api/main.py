from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from models import Book
from database import get_db, Base, engine
from schemas import BookCreate, BookResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/books/", response_model=BookResponse)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = Book(title=book.title, author=book.author, rating=book.rating)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.get("/books/", response_model=list[BookResponse])
def read_books(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return books
