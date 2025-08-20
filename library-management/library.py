import json
import os
import httpx
from book import Book

class Library:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = []
        self.load_books()

    def add_book(self, book: Book):
        # Aynı ISBN varsa hata
        if self.find_book(book.isbn):
            raise ValueError("Bu ISBN zaten mevcut.")
        self.books.append(book)
        self.save_books()

    def add_book_by_isbn(self, isbn: str):
        url = f"https://openlibrary.org/isbn/{isbn}.json"
        try:
            resp = httpx.get(url, timeout=10)
            resp.raise_for_status()
            data = resp.json()

            title = data.get("title", "Bilinmiyor")
            authors = []
            if "authors" in data:
                for a in data["authors"]:
                    author_data = httpx.get(f"https://openlibrary.org{a['key']}.json").json()
                    authors.append(author_data.get("name", "Bilinmeyen Yazar"))

            author = ", ".join(authors) if authors else "Bilinmeyen"
            book = Book(title, author, isbn)
            self.add_book(book)
            return book
        except Exception:
            raise ValueError("Kitap bilgisi alınamadı.")

    def remove_book(self, isbn: str):
        self.books = [b for b in self.books if b.isbn != isbn]
        self.save_books()

    def list_books(self):
        return self.books

    def find_book(self, isbn: str):
        return next((b for b in self.books if b.isbn == isbn), None)

    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.books = [Book(**item) for item in data]

    def save_books(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([vars(b) for b in self.books], f, ensure_ascii=False, indent=4)
