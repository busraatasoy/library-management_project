from fastapi.testclient import TestClient
from fastapi_main import app

client = TestClient(app)

def test_list_books():
    response = client.get("/books/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

