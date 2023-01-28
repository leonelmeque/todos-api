from flask import Flask, Blueprint, request, jsonify
from models.users import users
from helpers.lib import id_generator

user_routes = Blueprint('users', __name__)


@user_routes.post('/sign-up')
def user_signup():
    email = request.form.get('email')
    firstName = request.form.get('firstName')
    lastName = request.form.get('lastName')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    users.insert({
        "id": id_generator(),
        "username": email,
        "firstName": firstName,
        "lastName": lastName,
        "password": password1,
        "avatar": "",
    })

    return jsonify({"message": "User succesfuly create"}), 200


@user_routes.post('/login')
def user_login():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')

    users.insert({
        "email": email,
        "username": username,
        "password": password
    })

    return jsonify({"message": "User succesfully create", "result": {"email": email, "username": username}}), 200
