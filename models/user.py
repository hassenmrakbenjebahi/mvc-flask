
from flask_pymongo import PyMongo

mongo = PyMongo()
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


@staticmethod
def create_user(email, password, name):
        """
        Creates a new user document in the MongoDB database.
        """
        user_data = {
            "email": email,
            "password": password,
            "name": name,
        }
        result = mongo.db.users.insert_one(user_data)
        user_data['_id'] = str(result.inserted_id)  # Convert ObjectId to string
        return user_data