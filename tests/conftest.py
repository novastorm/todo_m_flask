import os
import pytest
import tempfile

from todo import create_app
from todo.database import get_database, init_db
from todo.clients.database_client import Database_Client


@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()

    config = {
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///%s' % db_path,
        'TESTING': True
    }

    app = create_app(config=config)

    with app.app_context():
        init_db()
        yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()
