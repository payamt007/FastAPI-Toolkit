def test_add_song(client, session):
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
