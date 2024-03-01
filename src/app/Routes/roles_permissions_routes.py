from flask import request
from app import app
from Controllers.roles_permissions import *

@app.route("/roles_permissions", methods=["GET"])
def get_roles_permissions_route():
    return get_roles_permissions()

@app.route("/roles_permissions/<role_id>", methods=["GET"])
def get_roles_permissions_byroleid_route(role_id):
    return get_role_permission(role_id)

@app.route("/roles_permissions", methods=["POST"])
def create_role_permission_route():
    return create_role_permission()

@app.route("/roles_permissions/<role_id>/<permission_id>", methods=["PUT"])
def update_role_permission_route(role_id, permission_id):
    return update_role_permission(role_id, permission_id)

@app.route("/roles_permissions/<role_id>/<permission_id>", methods=["DELETE"])
def delete_role_permission_route(role_id, permission_id):
    return delete_role_permission(role_id, permission_id)