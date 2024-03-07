import os
from datetime import UTC, datetime, timedelta
from typing import Annotated

import bcrypt
from fastapi import APIRouter, Depends, HTTPException, Security, status
from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm,
    SecurityScopes,
)
from jose import JWTError, jwt
from pydantic import BaseModel, ValidationError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import Session, select

from ..db import engine, get_db_session
from .models import User
from .schemas import UserCreate, UserRead

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = os.environ.get("SECRET_KEY") or "sample_secret_key_here!!!"
ALGORITHM = os.environ.get("ALGORITHM") or "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES") or 30

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token",
    scopes={"me": "Read information about the current user.", "items": "Read items."},
)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
    scopes: list[str] = []


def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password)


def get_password_hash(password: str):
    salt = bcrypt.gensalt(rounds=14)
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def get_user(username: str | None):
    with Session(engine) as session:
        # SQLModel.metadata.create_all(engine)
        result = session.exec(select(User).where(User.username == username))
        user = result.first()
        return user


def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(UTC) + expires_delta
    else:
        expire = datetime.now(UTC) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(
        security_scopes: SecurityScopes, token: Annotated[str, Depends(oauth2_scheme)]
):
    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = "Bearer"
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": authenticate_value},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_scopes = payload.get("scopes", [])
        token_data = TokenData(scopes=token_scopes, username=username)
    except (JWTError, ValidationError) as err:
        raise credentials_exception from err
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    for scope in security_scopes.scopes:
        if scope not in token_data.scopes:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not enough permissions",
                headers={"WWW-Authenticate": authenticate_value},
            )
    return user


async def get_current_active_user(
        current_user: Annotated[User, Security(get_current_user, scopes=["me"])],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@router.post("/token")
async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username, "scopes": form_data.scopes},
        expires_delta=access_token_expires,
    )
    return Token(access_token=access_token, token_type="bearer")


@router.get("/user", response_model=UserRead)
async def get_current_active_user_from_token(
        current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user


@router.post("/user", response_model=UserRead)
async def register_user(user: UserCreate, session: AsyncSession = Depends(get_db_session),
                        ):
    new_user = User(
        username=user.username,
        full_name=user.full_name,
        email=user.email,
        password=get_password_hash(user.password),
    )
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user
