import pytest
import sqlalchemy
from sqlalchemy import orm


@pytest.fixture(scope="module")
def session_fixture():
    engine = sqlalchemy.create_engine(url="postgresql://myuser:mypassword@localhost:5432/mydatabase")
    session_maker = orm.sessionmaker(bind=engine)
    session = session_maker()
    yield session
