import json
from pathlib import Path
from uuid import uuid4

path = Path(__file__).parent.resolve()
with open(path / "mock_data" / "users_response.json") as file:
    expected_response = json.load(file)


def test_healthcheck(client):
    response = client.get("/")

    assert response.ok
    assert response.text == '"OK"'


def test_get_users(client):
    response = client.get("/users")

    assert response.ok
    assert response.json() == expected_response


def test_get_users_limit(client):
    for i in range(0, 3):
        response_limits_option = client.get(f"/users?limit={i}")

        assert response_limits_option.ok
        assert len(response_limits_option.json()) == i


def test_get_users_offset(client):
    for i in range(0, 3):
        response_offset_option = client.get(f"/users?offset={i}")

        assert response_offset_option.ok
        assert response_offset_option.json() == expected_response[i:]


def test_get_user(client):
    response = client.get("/users/bfde8bae-5b25-495e-9e87-37ab1695f5ae")

    assert response.ok
    assert response.json() == expected_response[0]


def test_user_not_found(client):
    response = client.get(f"/users/{uuid4()}")

    assert response.status_code == 404


def test_user_not_valid(client):
    response = client.get("/users/labuda-labuda")

    assert response.status_code == 422


def test_create_user(client):
    request_json = {
        "first_name": "First name",
        "last_name": "Last name",
        "birthday": "2000-01-01",
    }
    response = client.post("/users", json=request_json)

    assert response.ok
    response_json = response.json()
    assert response_json.pop("id")
    assert request_json == response_json


def test_update_user(client):
    request_json = {
        "first_name": "First name Updated",
        "last_name": "Last name",
        "birthday": "2000-01-01",
    }
    response = client.patch(
        "/users/bfde8bae-5b25-495e-9e87-37ab1695f5ae", json=request_json
    )
    response_json = response.json()

    assert response.ok
    request_json["id"] = "bfde8bae-5b25-495e-9e87-37ab1695f5ae"
    assert request_json == response_json


def test_delete_user(client):
    expected_response = {
        "id": "bfde8bae-5b25-495e-9e87-37ab1695f5ae",
        "first_name": "First name Updated",
        "last_name": "Last name",
        "birthday": "2000-01-01",
    }
    response = client.delete("/users/bfde8bae-5b25-495e-9e87-37ab1695f5ae")
    response_json = response.json()

    assert response.ok
    assert expected_response == response_json
