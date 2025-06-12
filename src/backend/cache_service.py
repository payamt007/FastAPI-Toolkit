import os

from redis.asyncio import Redis

host = os.environ.get("REDIS_HOST") or "127.0.0.1"
port = int(os.environ.get("REDIS_PORT") or 6379)

r = Redis(host=host, port=port, decode_responses=True)
