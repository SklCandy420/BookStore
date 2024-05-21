def test_create_genre(client, auth_token):
    response = client.post(
        "/genres/",
        json={"name": "Test Genre"},
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Test Genre"


def test_read_genres(client, auth_token):
    response = client.get("/genres/", headers={"Authorization": f"Bearer {auth_token}"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_read_genre(client, auth_token):
    response = client.get(
        "/genres/1", headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_update_genre(client, auth_token):
    response = client.put(
        "/genres/1",
        json={"name": "Updated Test Genre"},
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Test Genre"


def test_delete_genre(client, auth_token):
    response = client.delete(
        "/genres/1", headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Genre deleted successfully"
