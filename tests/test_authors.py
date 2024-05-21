def test_create_author(client, auth_token):
    response = client.post(
        "/authors/",
        json={"name": "Test Author", "biography": "Test Biography"},
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Test Author"


def test_read_authors(client, auth_token):
    response = client.get(
        "/authors/", headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_read_author(client, auth_token):
    response = client.get(
        "/authors/1", headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_update_author(client, auth_token):
    response = client.put(
        "/authors/1",
        json={"name": "Updated Test Author", "biography": "Updated Biography"},
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Test Author"


def test_delete_author(client, auth_token):
    response = client.delete(
        "/authors/1", headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Author deleted successfully"
