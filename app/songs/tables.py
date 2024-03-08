from sqlalchemy import Column, Integer, String

from ..db import Base


class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True)
    name = Column(String)
