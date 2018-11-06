import pytest
from todo.clients.database_client import Database_Client
from todo.models.user import User

def test_database_client(client):

    dbClient = Database_Client()
    newUser = dbClient.createUser(username='test', password='asdf1234')
    dbClient.saveRecord(newUser)

    print("test")
    print(newUser)

    users = dbClient.getRecords(model=User)
    for user in users:
        print(user.serialize)
