from typing import Optional

from sqlmodel import Field, SQLModel


class SongBase(SQLModel):
    name: str
    artist: str
    description: Optional[str] = None
    year: Optional[int] = None


class Song(SongBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)
    city_id: Optional[int] = Field(default=None, foreign_key="city.id")


class SongCreate(SongBase):
    pass


class City(SQLModel, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)
    title: str
    desc: str
