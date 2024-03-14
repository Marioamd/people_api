from flask import request
from app import app
from app.Controllers.permissions import *

@app.route('/permissions', methods=['GET'])
def get_permissions_route():
    return get_permissions()

@app.route('/permissions/<id>', methods=['GET'])
def get_permissionbyid_route(id):
    return get_permission(id)

@app.route('/permissions', methods=['POST'])
def create_permission_route():
    return create_permission()

@app.route('/permissions/<id>', methods=['PUT'])
def update_permission_route(id):
    return update_permission(id)

@app.route('/permissions/<id>', methods=['DELETE'])
def delete_permission_route(id):
    return delete_permission(id)

