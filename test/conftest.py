# pylint: disable=unused-argument,redefined-outer-name
import os
import tempfile

import pytest

from app import app
from app import db


@pytest.fixture()
def test_db():
    """
    Temporal database for testing
    """
    db_fd, db_path = tempfile.mkstemp()
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_path
    app.config["TESTING"] = True

    db.create_all()
    db.session = db.create_scoped_session({"expire_on_commit": False})

    yield db

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(test_db):
    """
    Http client to perform requests in tests
    """
    with app.test_client() as client:
        yield client
