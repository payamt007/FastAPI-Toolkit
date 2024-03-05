from sqlalchemy import Column, Integer, String

from ..db import Base

# class BaseUser(SQLModel):
#     username: str
#     email: str | None = None
#     full_name: str | None = None
#     password: str
#
#
# class User(BaseUser, table=True):
#     id: int = Field(default=None, nullable=False, primary_key=True)
#     disabled: bool | None = None


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    full_name = Column(String)
    password = Column(String)
