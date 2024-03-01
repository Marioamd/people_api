from flask import request
from app import app
from Controllers.users import *

@app.route("/users", methods="GET")
def get_users_route():
    return get_users()

@app.route("/users/<id>", methods="GET")
def get_userbyid_route(id):
    return get_user(id)

@app.route("/users", methods="POST")
def create_user_route():
    return create_user()

@app.route("/users/<id>", methods="PUT")
def update_user_route(id):
    return create_user(id)

@app.route("/users/<id>", methods="DELETE")
def delete_user_route(id):
    return delete_user(id)

