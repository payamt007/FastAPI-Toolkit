from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session, select

from ..auth.handlers import get_current_active_user
from ..auth.models import User
from ..db import engine
from .models import Song, SongCreate

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/songs", response_model=list[Song])
async def get_songs(current_user: Annotated[User, Depends(get_current_active_user)]):
    with Session(engine) as session:
        songs = session.exec(select(Song)).all()
        return [Song(name=song.name, artist=song.artist, year=song.year, id=song.id, description=song.description) for
                song
                in songs]


@router.post("/songs")
async def add_song(song: SongCreate):
    with Session(engine) as session:
        song = Song(name=song.name, artist=song.artist, year=song.year, description=song.description)
        session.add(song)
        session.commit()
        session.refresh(song)
        return song
