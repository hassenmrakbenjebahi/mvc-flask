# pseudo code
import sys
from flask import render_template, redirect, url_for, request, abort, jsonify
from models.user import User
from flask_pymongo import PyMongo
from services.userService import save_user_to_mongo


def add_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    save_user_to_mongo(name, email, password)
    return jsonify({"message": "User added successfully"}), 201
        

