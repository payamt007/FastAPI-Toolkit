# FastAPI + SQLModel + Alembic
This project is a opinionated boilerplate for FastAPI micro framework that uses async SQLAlchemy, SQLModel, PostgresSQL, Alembic, and Docker. You can use this ready to use sample and don't worry abuot CI pipelines and running database migrations and tests inside a FastAPI project.


## Want to use this project?

```sh
$ docker-compose up -d --build
```


Add a song:

```sh
$ curl -d '{"name":"ALen Fit", "artist":"Helen", "year":"2015"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8001/songs
```

Get all songs: [http://127.0.0.1:8001/songs](http://localhost:8004/songs)

## Want to Run tests?

```sh
$ docker compose exec api pytest
```