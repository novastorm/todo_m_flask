from __future__ import absolute_import
from todo.db import get_db, table_prefix

db = get_db()

class User(db.Model):
    __tablename__ = '%s%s' % (table_prefix, 'user')

    class keys:
        id = 'id'
        username = 'username'
        password = 'password'
        todos = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)

    todos = db.relationship('Todo', back_populates='user')


    @property
    def serialize(self):
        return {
            self.keys.id: self.id,
            self.keys.username: self.username
        }
    