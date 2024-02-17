
from flask_pymongo import PyMongo
from models.user import User
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

mongo = PyMongo(app)

def save_user_to_mongo(name, email, password):
    user = User(name, email, password)
    mongo.db.users.insert_one(
        {"name": user.name, "email": user.email, "password": user.password}
    )


