from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List
import json
import os

app = FastAPI(title="Library API")

DATA_FILE = "library.json"

class Book(BaseModel):
    title: str
    author: str
    isbn: str


def load_books() -> List[Book]:
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Book(**book) for book in data]
    return []


def save_books(books: List[Book]):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([book.dict() for book in books], f, indent=4, ensure_ascii=False)


books_db: List[Book] = load_books()


@app.get("/")
def root():
    return {"message": "📚 Library Management API'ye hoş geldiniz! /docs adresinden deneyebilirsiniz."}


@app.get("/books/", response_model=List[Book])
def list_books():
    return books_db


@app.post("/books/", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book: Book):
    # Aynı ISBN varsa ekleme
    for b in books_db:
        if b.isbn == book.isbn:
            raise HTTPException(status_code=400, detail="Bu ISBN zaten mevcut.")
    books_db.append(book)
    save_books(books_db)
    return book


@app.get("/books/{isbn}", response_model=Book)
def get_book(isbn: str):
    for book in books_db:
        if book.isbn == isbn:
            return book
    raise HTTPException(status_code=404, detail="Kitap bulunamadı")


@app.delete("/books/{isbn}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(isbn: str):
    global books_db
    for i, book in enumerate(books_db):
        if book.isbn == isbn:
            books_db.pop(i)
            save_books(books_db)
            return
    raise HTTPException(status_code=404, detail="Kitap bulunamadı")
