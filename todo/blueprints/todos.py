from __future__ import absolute_import
from flask import (
    Blueprint, abort, flash, g, jsonify, redirect, render_template, request,
    session, url_for
    )

bp = Blueprint('todos', __name__, url_prefix='/todos')

routeTitle = 'Todos'


@bp.route('/')
def show_index_view():
    return '%s show_index_view' % routeTitle


@bp.route('/<int:todo_id>')
def show_record_view(todo_id):
    return '%s show_record_view [%s]' % (routeTitle, todo_id)


@bp.route('/create')
def show_create_view():
    return '%s show_create_view' % routeTitle


@bp.route('/<int:todo_id>/edit')
def show_edit_view(todo_id):
    return '%s show_edit_view [%s]' % (routeTitle, todo_id)


@bp.route('/<int:todo_id>/delete')
def show_delete_view(todo_id):
    return '%s show_delete_view [%s]' % (routeTitle, todo_id)


@bp.route('/', methods=['post'])
def create_record():
    return '%s create_record' % routeTitle


@bp.route('/<int:todo_id>', methods=['put'])
def update_record(todo_id):
    return '%s update_record [%s]' % (routeTitle, todo_id)


@bp.route('/<int:todo_id>', methods=['delete'])
def delete_record(todo_id):
    return '%s delete_record [%s]' % (routeTitle, todo_id)
