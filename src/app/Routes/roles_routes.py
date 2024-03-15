from flask import request
from app import app
from app.Controllers.roles import *
from app.Services.security import token_required

@app.route('/roles', methods=['GET'])
@token_required
def get_roles_route():
    return get_roles()

@app.route('/roles/<id>', methods=['GET'])
@token_required
def get_rolebyid_route(id):
    return get_role(id)

@app.route('/roles', methods=['POST'])
@token_required
def create_role_route():
    return create_role()

@app.route('/roles/<id>', methods=['PUT'])
@token_required
def update_role_route(id):
    return update_role(id)

@app.route('/roles/<id>', methods=['DELETE'])
@token_required
def delete_role_route(id):
    return delete_role(id)
