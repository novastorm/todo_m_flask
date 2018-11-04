import os
from flask import Flask, g

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


    from . import database
    database.init_app(app)

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
