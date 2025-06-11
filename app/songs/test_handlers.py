import pytest
from sqlalchemy import select
from app.songs.models import Song


@pytest.mark.asyncio
async def test_add_song(client, session):
    payload = {
        "name": "Test Song",
        "artist": "Test Artist",
        "year": 2023,
        "description": "A test song description"
    }

    # Send request to add a song
    response = client.post("/songs", json=payload)

    # Check response
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == payload["name"]
    assert data["artist"] == payload["artist"]
    assert data["year"] == payload["year"]
    assert data["description"] == payload["description"]
    assert "id" in data

    # Verify the record exists in the database
    song_id = data["id"]
    result = await session.execute(select(Song).where(Song.id == song_id))
    db_song = result.scalar_one()

    # Assert that db record matches the payload
    assert db_song.name == payload["name"]
    assert db_song.artist == payload["artist"]
    assert db_song.year == payload["year"]
    assert db_song.description == payload["description"]
