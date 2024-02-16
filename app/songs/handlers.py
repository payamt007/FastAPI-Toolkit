from fastapi import Depends, APIRouter
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from ..db import get_session
from .models import Song, SongCreate

router = APIRouter()


@router.get("/songs", response_model=list[Song])
async def get_songs(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Song))
    songs = result.scalars().all()
    return [Song(name=song.name, artist=song.artist, year=song.year, id=song.id) for song in songs]


@router.post("/songs")
async def add_song(song: SongCreate, session: AsyncSession = Depends(get_session)):
    song = Song(name=song.name, artist=song.artist, year=song.year)
    session.add(song)
    await session.commit()
    await session.refresh(song)
    return song
