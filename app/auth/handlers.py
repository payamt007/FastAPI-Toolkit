from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from ..db import get_session
from .models import User

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/user", response_model=User | None)
# token: Annotated[str, Depends(oauth2_scheme)],
async def get_user(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(User))
    user = result.scalars().first()
    return user
