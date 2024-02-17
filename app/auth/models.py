from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None
