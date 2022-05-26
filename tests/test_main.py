import json
from pathlib import Path

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

path = Path(__file__).parent.resolve()
with open(path / "mock_data" / "users_response.json") as file:
    expected_response = json.load(file)


def test_healthcheck():
    response = client.get("/")

    assert response.ok
    assert response.text == '"OK"'


def test_get_users():
    response = client.get("/users")

    assert response.ok
    assert response.json() == expected_response


def test_get_users_limit():
    for i in range(0, 3):
        response_limits_option = client.get(f"/users?limit={i}")

        assert response_limits_option.ok
        assert len(response_limits_option.json()) == i


def test_get_users_offset():
    for i in range(0, 3):
        response_offset_option = client.get(f"/users?offset={i}")

        assert response_offset_option.ok
        assert response_offset_option.json() == expected_response[i:]
