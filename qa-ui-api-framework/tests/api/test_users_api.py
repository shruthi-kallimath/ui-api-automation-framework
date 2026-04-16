def test_get_users_list(api_client):
    response = api_client.get("/users?page=2")

    assert response.status_code == 200

    response_json = response.json()
    assert "data" in response_json
    assert len(response_json["data"]) > 0


def test_single_user(api_client):
    response = api_client.get("/users/2")

    assert response.status_code == 200

    response_json = response.json()
    assert response_json["data"]["id"] == 2