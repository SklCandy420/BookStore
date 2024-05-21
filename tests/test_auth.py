def test_create_user(client):
    response = client.post(
        "/auth/create/user/", json={"username": "newuser", "password": "newpassword"}
    )
    assert response.status_code == 200
    assert response.json()["username"] == "newuser"


def test_login_for_access_token(client, create_test_user):
    response = client.post(
        "/auth/token",
        data={
            "username": create_test_user["username"],
            "password": create_test_user["password"],
        },
    )
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_read_users_me(client, auth_token):
    response = client.get(
        "/auth/users/me", headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"
