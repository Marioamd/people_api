from flask import request
from app import app
from Controllers.roles import *

@app.route("/roles", methods="GET")
def get_roles_route():
    return get_roles()

@app.route("/roles/<id>", methods="GET")
def get_rolebyid_route(id):
    return get_role(id)

@app.route("/roles", methods="POST")
def create_role_route():
    return create_role()

@app.route("/roles/<id>", methods="PUT")
def update_role_route(id):
    return update_role(id)

@app.route("/roles/<id>", methods="DELETE")
def delete_role_route(id):
    return delete_role(id)