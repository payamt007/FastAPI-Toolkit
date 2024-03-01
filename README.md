# FastAPI + SQLModel + Alembic + Celery + MongoDB + Redis + jwt Auth

This project is an opinionated boilerplate for **FastAPI** micro framework that uses  **_SQLAlchemy_**,
_**SQLModel**_, **_PostgresSQL_**, _**Alembic**_, **_Celery_**, **_MongoDB_**, _**Redis**_, **_Docker_** and *
*_jwt Authentication_**. You can use this ready to
use sample and don't worry about CI pipelines and running database migrations and tests inside a FastAPI project.

## Add new tables to PostgresSQL database :

```sh
git clone https://github.com/payamt007/FastAPI-Toolkit
cd FastAPI-Toolkit/app
```

Then create new folder (for example artists) in `app` directory

```sh
cd artists
````

Create `__init__.py` file and a empty `models.py` file inside folder
and paste this sample content inside `models.py` file:

```python 
from sqlmodel import Field, SQLModel


class Artist(SQLModel, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)
    name: str
    city: str
```

go to `migrations/env.py` folder in root directory and add this content to it:

```python
from app.artists.models import Artist
```

then run new migration command in root directory:

```sh
alembic revision --autogenerate -m "added_artist_model"
alembic upgrade head
````

## Want to run this project?

```sh
$ docker-compose up -d --build
```

## Project Swagger:

[http://127.0.0.0:8001/docs](http://127.0.0.0:8001)

### Add a song:

```sh
$ curl -d '{"name":"ALen Fit", "artist":"Helen", "year":"2015"}' -H "Content-Type: application/json" -X POST http://127.0.0.2:8001/songs
```

### Get all songs:

[http://127.0.0.0:8001/songs](http://localhost:8004/songs)

## Run tests

```sh
$ docker compose exec api pytest
```