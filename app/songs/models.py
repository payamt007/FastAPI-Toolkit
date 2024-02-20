from typing import Optional

from pydantic import field_validator
from sqlmodel import Field, Relationship, SQLModel


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


class City(SQLModel, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)
    title: str
    desc: str

    songs: list["Song"] = Relationship(back_populates="city")


class Song(SongBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)

    city: Optional["City"] = Relationship(back_populates="songs")


class SongCreate(SongBase):
    pass
