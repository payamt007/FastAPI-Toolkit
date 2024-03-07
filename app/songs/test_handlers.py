import pytest


@pytest.mark.asyncio
async def test_add_song(client):
    response = await client.post(
        "/songs",
        json={"name": "Alen", "artist": "test", "year": 1960},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "Alen"
    assert data["artist"] == "test"
    assert data["year"] == 1960
    assert "id" in data
