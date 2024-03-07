from sqlalchemy import Column, Integer, String

from ..db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    full_name = Column(String)
    password = Column(String)
