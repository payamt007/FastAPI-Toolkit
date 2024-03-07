from typing import Optional

from pydantic import BaseModel, field_validator


class SongRead(BaseModel):
    id: int
    name: str
    artist: str
    description: str | None = None
    year: int | None = None
    city: Optional["City"]
    tags: list["Tag"]


class SongBase(BaseModel):
    name: str
    artist: str
    description: str | None
    year: int | None
    city_id: int | None

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


class CityCreate(BaseModel):
    name: str


class CityRead(CityCreate):
    id: int


class TagCreate(BaseModel):
    title: str
    description: str


class TagRead(TagCreate):
    id: int
