from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    email: str
    full_name: str
    password: str
