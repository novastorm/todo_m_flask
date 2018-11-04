import click
from flask import current_app, g
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import find_modules, import_string

table_prefix = 'todo_'

class keys:
    database = 'db'


def get_db():
    if keys.database not in g:
        g.db = SQLAlchemy(current_app)

    return g.db

def init_db():
    db = get_db()
    for name in find_modules('todo.models', recursive=True):
        print(name)
        mod = import_string(name)
    db.create_all()


def close_db(e=None):
    db = g.pop(keys.database, None)

    if db is not None:
        db.session.close()


@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Database initialized.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)