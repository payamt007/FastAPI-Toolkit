from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped

from ..db import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = Column(Integer, primary_key=True)
    username: Mapped[str] = Column(String)
    email: Mapped[str] = Column(String)
    full_name: Mapped[str | None] = Column(String)
    password: Mapped[str] = Column(String)
