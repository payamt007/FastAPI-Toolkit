from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .auth.handlers import router as auth_router
from .files.handlers import router as files_router
from .live_socket.handlers import router as ws_router
from .songs.handlers import router as song_router

app = FastAPI()

app.include_router(song_router)
app.include_router(auth_router)
app.include_router(files_router)
app.include_router(ws_router)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}
