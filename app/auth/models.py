from __future__ import annotations

from sqlmodel import Field, SQLModel


class BaseUser(SQLModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    password: str


class User(BaseUser, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)
    disabled: bool | None = None
