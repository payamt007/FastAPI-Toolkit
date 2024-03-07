from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..db import Base


class SongTag(Base):
    __tablename__ = "song_tag"

    song_id: Mapped[int] = mapped_column(ForeignKey("songs.id"), primary_key=True)
    tag_id: Mapped[int] = mapped_column(ForeignKey("tags.id"), primary_key=True)


class Song(Base):
    __tablename__ = "songs"

    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String)
    artist: Mapped[str] = Column(String)
    description: Mapped[str] = Column(String)
    year: Mapped[str] = Column(String)
    city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"))

    city: Mapped["City"] = relationship("City", back_populates="songs")
    tags: Mapped[list["Tag"]] = relationship("Tag", back_populates="songs", secondary=SongTag.__table__)


class Tag(Base):
    __tablename__ = "tags"
    id: Mapped[int] = Column(Integer, primary_key=True)

    title: Mapped[str] = Column(String)
    description: Mapped[str] = Column(String)

    songs: Mapped[list["Song"]] = relationship(back_populates="tags", secondary=SongTag.__table__)


class City(Base):
    __tablename__ = "cities"

    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String)

    songs: Mapped[list["Song"]] = relationship("Song", back_populates="city")
