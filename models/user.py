
from flask_pymongo import PyMongo

mongo = PyMongo()
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


