from flask import request
from app import app
from app.Controllers.auth import *

@app.route('/login', methods=['POST'])
def login_route():
    return login()