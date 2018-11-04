from __future__ import absolute_import
import functools
from flask import (
    Blueprint, abort, flash, g, jsonify, redirect, render_template, request,
    session, url_for
    )
from werkzeug.security import check_password_hash, generate_password_hash

from todo.database import get_database

from todo.models.user import User
from todo.models.todo import Todo

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)


@bp.route('/register')
def show_register_view():
    return render_template('auth/register.html')


@bp.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    db = get_database()
    error = None

    if not username or not password:
        error = 'Username and Password are required'
    elif User.query.filter_by(username=username).one_or_none() is not None:
        error = 'Username {} is already registered.'.format(username)

    if error is None:
        newUser = User(username=username, password=generate_password_hash(password))
        db.session.add(newUser)
        db.session.commit()

        return redirect(url_for('auth.show_login_view'))

    flash(error)
    return render_template('auth/register.html')


@bp.route('/login')
def show_login_view():
    return render_template('auth/login.html')


@bp.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    db = get_database()
    error = None
    user = User.query.filter_by(username=username).one_or_none()

    if user is None:
        error = 'Incorrect username.'
    elif not check_password_hash(user.password, password):
        error = 'Incorrect password.'

    if error is None:
        session.clear()
        session['user_id'] = user.id
        return redirect(url_for('main.index'))

    flash(error)
    return render_template('auth/login.html')


@bp.route('/logout')
def logout():
    session.clear()
    return(url_for('main.index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.show_login_view'))
        return view(**kwargs)

    return wrapped_view
