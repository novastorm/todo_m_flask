from __future__ import absolute_import
from todo.database import get_database, table_prefix

# from todo.models.user import User

db = get_database()

class Todo(db.Model):
    __tablename__ = '%s%s' % (table_prefix, 'todo')

    class keys:
        id = 'id'
        user_id = 'user_id'
        created = 'created'
        title = 'title'
        body = 'body'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('%s%s' % (table_prefix, 'user.id')), nullable=False)
    created = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
    title = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=False)

    user = db.relationship('User', back_populates='todos')


    @property
    def serialize(self):
        return {
            self.keys.id: self.id,
            self.keys.user_id: self.user_id,
            self.keys.created: self.created,
            self.keys.title: self.title,
            self.keys.body: self.body
        }
    