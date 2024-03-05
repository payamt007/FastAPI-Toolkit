from typing import Optional

from pydantic import field_validator
from sqlmodel import Field, Relationship, SQLModel


class SongTag(SQLModel, table=True):
    song_id: int | None = Field(default=None, foreign_key="song.id", primary_key=True)
    tag_id: int | None = Field(default=None, foreign_key="tag.id", primary_key=True)


class SongBase(SQLModel):
    name: str
    artist: str
    description: str | None = None
    year: int | None = None
    city_id: int | None = Field(default=None, foreign_key="city.id")

    @field_validator("year")
    @classmethod
    def validate_year(cls, value):
        if value is not None and value < 1900:
            raise ValueError("Year must be 1900 or later")
        return value

    @field_validator("description")
    @classmethod
    def validate_description(cls, value):
        if value is not None and len(value) < 5:
            raise ValueError("Description must be at least 5 characters long")
        return value


class SongCreate(SongBase):
    pass


class Song(SongBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)

    city: Optional["City"] = Relationship(back_populates="songs")
    tags: list["Tag"] = Relationship(back_populates="songs", link_model=SongTag)


class SongRead(SQLModel):
    id: int
    name: str
    artist: str
    description: str | None = None
    year: int | None = None
    city: Optional["City"]
    tags: list["Tag"]


class TagCreate(SQLModel):
    title: str
    description: str


class Tag(TagCreate, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)

    songs: list["Song"] = Relationship(back_populates="tags", link_model=SongTag)


class CityCreate(SQLModel):
    title: str
    desc: str


class City(CityCreate, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)

    songs: list["Song"] = Relationship(back_populates="city")

