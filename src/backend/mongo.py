import os

import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient(
    os.environ.get("MONGODB_URL") or "mongodb://localhost:27017"
)
db = client.college
