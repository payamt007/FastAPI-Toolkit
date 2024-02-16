from fastapi import Depends, FastAPI

from .songs.handlers import router as song_router

app = FastAPI()

app.include_router(song_router)


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}
