from __future__ import absolute_import
from flask import (
    Blueprint, abort, flash, g, jsonify, redirect, render_template, request,
    session, url_for
    )

from todo.database import get_database

bp = Blueprint('todo', __name__, url_prefix='/todo')

# @bp.route('/')
# def index_todo():
#     return 'index todo'
    