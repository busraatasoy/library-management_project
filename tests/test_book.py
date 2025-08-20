from book import Book

def test_book_str():
    b = Book("Ulysses", "James Joyce", "12345")
    assert str(b) == "Ulysses by James Joyce (ISBN: 12345)"
