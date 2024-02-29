# FastAPI + SQLModel + Alembic

This project is an opinionated boilerplate for **FastAPI** micro framework that uses  **_SQLAlchemy_**, 
_**SQLModel**_, **_PostgresSQL_**, _**Alembic**_, **_Celery_**, _**Redis**_ and **_Docker_**. You can use this ready to
use sample and don't worry about CI pipelines and running database migrations and tests inside a FastAPI project.

## Add new revision for database :

```sh
alembic revision --autogenerate -m "init"

alembic upgrade head
```

## Want to use this project?

```sh
$ docker-compose up -d --build
```

## Project Swagger:

[http://127.0.0.0:8001/docs](http://127.0.0.0:8001)


### Add a song:

```sh
$ curl -d '{"name":"ALen Fit", "artist":"Helen", "year":"2015"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8001/songs
```

### Get all songs:

[http://127.0.0.0:8001/songs](http://localhost:8004/songs)

## Run tests

```sh
$ docker compose exec api pytest
```