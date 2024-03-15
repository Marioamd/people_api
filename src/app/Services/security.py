import jwt
import datetime
from flask import Flask
from dotenv import dotenv_values
import bcrypt

config = dotenv_values('.env')
secret_key = config['JWT_KEY']

class Security():

    @staticmethod
    def generate_token(authenticated_user):
        expiration_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
        payload = {
            'email': authenticated_user.email,
            'exp': expiration_time
        }
        return jwt.encode(payload, secret_key, algorithm='HS256')

    @staticmethod
    def verify_token(token):
        try:
            payload = jwt.decode(token, secret_key, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None

    @staticmethod
    def hash_password(password):
       
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        return hashed_password.decode('utf-8')  