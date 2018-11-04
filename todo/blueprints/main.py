from __future__ import absolute_import

from flask import (
    Blueprint, abort, flash, g, jsonify, redirect, render_template, request,
    session, url_for
    )

bp = Blueprint('main', __name__)

@bp.route('/hello')
def hello():
    return 'Hello, World!'
