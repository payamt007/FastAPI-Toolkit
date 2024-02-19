from __future__ import annotations

from fastapi import FastAPI

from .auth.handlers import router as auth_router
from .songs.handlers import router as song_router

app = FastAPI()

app.include_router(song_router)
app.include_router(auth_router)


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}
