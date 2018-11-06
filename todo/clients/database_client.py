from __future__ import absolute_import
from todo.database import db
from todo.models.user import User

class Database_Client:

    @classmethod
    def getRecords(cls, model, options=None):
        return model.query.all()


    @classmethod
    def createUser(cls, **kwargs):
        return User(**kwargs)


    @classmethod
    def saveRecord(cls, record):            
        db.session.add(record)
        db.session.commit()
