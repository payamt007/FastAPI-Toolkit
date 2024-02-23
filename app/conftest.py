import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine

from .db import get_session
from .main import app


@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(
        "sqlite:///testing.db", connect_args={"check_same_thread": False}
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture(name="client")
def client_fixture(session: Session):
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override

    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()
