from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from ..db import get_db_session
from .models import City, Song, Tag
from .schemas import CityCreate, CityRead, SongCreate, SongRead, TagCreate, TagRead

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/songs", response_model=list[SongRead])
async def get_songs(
        session: AsyncSession = Depends(get_db_session)):
    result = await session.scalars(select(Song).options(selectinload(Song.tags), selectinload(Song.city)))
    songs = result.all()
    return songs


@router.post("/songs")
async def add_song(song: SongCreate, session: AsyncSession = Depends(get_db_session)):
    new_song = Song(
        name=song.name,
        artist=song.artist,
        year=song.year,
        description=song.description,
    )
    session.add(new_song)
    await session.commit()
    return new_song


@router.post("/city", response_model=CityRead)
async def create_city(*, session: AsyncSession = Depends(get_db_session), city: CityCreate):
    # new_city = City(**city.dict())
    new_city = City(name=city.name)
    session.add(new_city)
    await session.commit()
    await session.refresh(new_city)
    return new_city


@router.post("/connect_city_with_song")
async def connect_city_with_song(
        city_title: str, song_title: str, session: AsyncSession = Depends(get_db_session)
):
    city_in_db = await session.scalars(select(City).where(City.name == city_title))
    city = city_in_db.first()
    song_in_db = await session.scalars(select(Song).where(Song.name.like(f"%{song_title}%")))
    song = song_in_db.first()
    song.city = city
    session.add(song)
    await session.commit()
    await session.refresh(song)
    return {"done": True}


@router.post("/tags", response_model=TagRead)
async def create_tag(*, session: AsyncSession = Depends(get_db_session), tag: TagCreate):
    input_tag = TagCreate.model_validate(tag)
    new_tag = Tag(**input_tag.dict())
    session.add(new_tag)
    await session.commit()
    await session.refresh(new_tag)
    return new_tag


@router.post("/attach-tags")
async def attach_tag_to_song(
        tag_title: str, song_name: str, session: AsyncSession = Depends(get_db_session)
):
    tag_in_db = await session.scalars(
        select(Tag).where(Tag.title.like(f"%{tag_title}%"))
    )
    tag = tag_in_db.first()
    song_in_db = await session.scalars(
        select(Song).options(selectinload(Song.tags)).where(Song.name.like(f"%{song_name}%")))
    song = song_in_db.first()
    song.tags.append(tag)
    session.add(tag)
    await session.commit()
    await session.refresh(song)
    return {"done": True}


@router.post("/redis")
def save_in_redis(key: str, value: str):
    r.set(key, value)
    return {"done": True}
