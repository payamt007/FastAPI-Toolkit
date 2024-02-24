from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session, select

from ..auth.handlers import get_current_active_user
from ..auth.models import User
from ..db import get_session
from ..redis import r
from .models import City, CityCreate, Song, SongCreate, SongRead, Tag, TagCreate

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/songs", response_model=list[SongRead])
async def get_songs(
    current_user: Annotated[User, Depends(get_current_active_user)],
    session: Session = Depends(get_session),
):
    songs = session.exec(select(Song)).all()
    return songs
    # songs = session.exec(select(Song, City.title).join(City, isouter=True)).all()
    # current_user: Annotated[User, Depends(get_current_active_user)],
    # return [
    #     {"name": song[0].name,
    #      "artist": song[0].artist,
    #      "year": song[0].year,
    #      "id": song[0].id,
    #      "description": song[0].description,
    #      "city": song[1]}
    #     for song in songs
    # ]


@router.post("/songs")
async def add_song(song: SongCreate, session: Session = Depends(get_session)):
    new_song = Song(
        name=song.name,
        artist=song.artist,
        year=song.year,
        description=song.description,
    )
    session.add(new_song)
    session.commit()
    session.refresh(new_song)
    return new_song


@router.post("/city", response_model=City)
def create_city(*, session: Session = Depends(get_session), city: CityCreate):
    new_city = City.model_validate(city)
    session.add(new_city)
    session.commit()
    session.refresh(new_city)
    return new_city


@router.post("/connect_city_with_song", response_model=Song)
def connect_city_with_song(
    city_title: str, song_title: str, session: Session = Depends(get_session)
):
    city_in_db = session.exec(select(City).where(City.title == city_title)).first()
    song = session.exec(select(Song).where(Song.name.like(f"%{song_title}%"))).first()
    song.city = city_in_db
    session.add(song)
    session.commit()
    session.refresh(song)
    return song


@router.post("/tags", response_model=Tag)
def create_tag(*, session: Session = Depends(get_session), tag: TagCreate):
    new_tag = Tag.model_validate(tag)
    session.add(new_tag)
    session.commit()
    session.refresh(new_tag)
    return new_tag


@router.post("/attach-tags")
def attach_tag_to_song(
    tag_title: str, song_name: str, session: Session = Depends(get_session)
):
    tag_in_db = session.exec(
        select(Tag).where(Tag.title.like(f"%{tag_title}%"))
    ).first()
    song_in_db = session.exec(
        select(Song).where(Song.name.like(f"%{song_name}%"))
    ).first()
    song_in_db.tags.append(tag_in_db)
    session.add(song_in_db)
    session.commit()
    session.refresh(song_in_db)
    return {"done": True}


@router.post("/redis")
def save_in_redis(key: str, value: str):
    r.set(key, value)
    return {"done": True}
