from __future__ import absolute_import
from flask import (
    Blueprint, abort, flash, g, jsonify, redirect, render_template, request,
    session, url_for
    )

from todo.database import get_database

bp = Blueprint('api_v0_todos', __name__, url_prefix='/api/v0/todos')

routeTitle = 'API Todos'


@bp.route('/')
def api_get_index():
    return '%s api_get_index' % routeTitle


@bp.route('/<int:todo_id>')
def api_get_record(todo_id):
    return '%s api_get_record [%s]' % (routeTitle, todo_id)


@bp.route('/', methods=['post'])
def api_store_record():
    return '%s api_store_record' % routeTitle


@bp.route('/<int:todo_id>', methods=['put'])
def api_update_record(todo_id):
    return '%s api_update_record [%s]' % (routeTitle, todo_id)


@bp.route('/<int:todo_id>', methods=['delete'])
def api_delete_record(todo_id):
    return '%s api_delete_record [%s]' % (routeTitle, todo_id)
