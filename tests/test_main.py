import json
from pathlib import Path

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_healthcheck():
    response = client.get("/")

    assert response.ok
    assert response.text == '"OK"'


def test_get_users():
    response = client.get("/users")
    assert response.ok

    path = Path(__file__).parent.resolve()

    with open(path / "mock_data" / "users_response.json") as file:
        expected_response = json.load(file)

    assert response.json() == expected_response
