from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"
mongo = PyMongo(app)

class User:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def save_to_mongo(self):
        mongo.db.users.insert_one(
            {"name": self.name, "age": self.age, "address": self.address}
        )

# Utilisation de l'exemple ci-dessus
user = User("Navindu", 22, "Colombo")
user.save_to_mongo()