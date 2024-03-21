from flask import request, jsonify
from app.Models.users_model import Users
from app.Services.authservice import AuthService
from app.Services.security import Security


def login():
    email = request.json['email']
    password = request.json['password']
    
    if not (email and password):
        return jsonify({'message': 'Missing email or password'}), 400

    _user = Users(None,None,None,None, email, password, None,None,None,None,None,None)
    authenticated_user = AuthService.login_user(_user)

    if (authenticated_user != None):
        encoded_token = Security.generate_token(authenticated_user)
        return jsonify({'success': True, 'token': encoded_token})
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401