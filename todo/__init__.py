from __future__ import absolute_import
import os
from flask import Flask, g
from werkzeug.utils import find_modules, import_string

def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.update(
        SQLALCHEMY_DATABASE_URI='sqlite:///%s/%s' % (app.instance_path, 'todo.sqlite'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        DEBUG=True,
        SECRET_KEY='dev',
        )

    if config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.update(config or {})

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    register_blueprints(app)
    register_database(app)

    return app


def register_database(app):
    from . import database
    database.init_app(app)


def register_blueprints(app):
    """Register all blueprint modules
    Reference: Armin Ronacher, "Flask for Fun and for Profit" PyBay 2016.
    """
    for name in find_modules('%s.%s' % (__name__, 'blueprints'), recursive=True):
        mod = import_string(name)
        if hasattr(mod, 'bp'):
            app.register_blueprint(mod.bp)
    return None
