def test_create_book(client, auth_token):
    response = client.post(
        "/books/",
        json={
            "title": "Test Book",
            "author_id": 1,
            "genre_id": 1,
            "publication_date": "2022-01-01",
            "price": 9.99,
        },
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Test Book"


def test_read_books(client, auth_token):
    response = client.get("/books/", headers={"Authorization": f"Bearer {auth_token}"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_read_book(client, auth_token):
    response = client.get("/books/1", headers={"Authorization": f"Bearer {auth_token}"})
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_update_book(client, auth_token):
    response = client.put(
        "/books/1",
        json={
            "title": "Updated Test Book",
            "author_id": 1,
            "genre_id": 1,
            "publication_date": "2022-01-01",
            "price": 9.99,
        },
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Test Book"


def test_delete_book(client, auth_token):
    response = client.delete(
        "/books/1", headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Book deleted successfully"
