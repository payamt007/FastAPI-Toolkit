import asyncio
import os

import bcrypt
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine

DATABASE_URL = os.environ.get("DATABASE_URL") or "sqlite:///database.db"
admin_username = os.environ.get("ADMIN_USERNAME") or "admin"
admin_password = os.environ.get("ADMIN_PASSWORD") or "admin"
engine = create_async_engine(DATABASE_URL, echo=True)


async def save_admin_user_in_db():
    salt = bcrypt.gensalt(rounds=14)
    hashed_passw = bcrypt.hashpw(admin_password.encode('utf-8'), salt)
    async with engine.begin() as conn:
        await conn.execute(
            text('INSERT INTO "users" (username, password) VALUES (:x, :y)'),
            [{"x": admin_username, "y": hashed_passw.decode("utf-8")}],
        )
        await conn.commit()


asyncio.run(save_admin_user_in_db())
