from flask import  request, jsonify
from services.userService import save_user_to_mongo


def add_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    save_user_to_mongo(name, email, password)
    return jsonify({"message": "User added successfully"}), 201

def yalla():
    return jsonify({"message": "architecture jawha behi "}), 201