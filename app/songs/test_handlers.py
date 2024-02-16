from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


def test_add_song():
    response = client.post(
        "/songs",
        json={"name": "Alen",
              "artist": "test",
              "year": 1960},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "Alen"
    assert data["artist"] == "test"
    assert data["year"] == 1960
    assert "id" in data
