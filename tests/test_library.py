import pytest
from book import Book
from library import Library

@pytest.fixture
def tmp_library(tmp_path):
    file = tmp_path / "test.json"
    return Library(filename=file)

def test_add_and_find_book(tmp_library):
    book = Book("Test", "Author", "111")
    tmp_library.add_book(book)
    assert tmp_library.find_book("111").title == "Test"

def test_remove_book(tmp_library):
    book = Book("Test Book", "Author", "111")
    tmp_library.add_book(book)
    tmp_library.remove_book("111")
    assert tmp_library.find_book("111") is None
