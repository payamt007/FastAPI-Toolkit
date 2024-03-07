import pytest
from httpx import AsyncClient

from ..main import app


@pytest.mark.asyncio
async def test_add_song():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        response = await ac.post(
            "/songs",
            json={"name": "Alen", "artist": "test", "year": 1960},
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["name"] == "Alen"
        assert data["artist"] == "test"
        assert data["year"] == 1960
        assert "id" in data
