from app.Models.users_model import Users
import bcrypt

class AuthService():
    @staticmethod
    def login_user(user):
        try:
            user_from_db = Users.query.filter_by(email=user.email).first()

            if user_from_db and bcrypt.checkpw(user.password.encode('utf-8'), user_from_db.password.encode('utf-8')):
                return user_from_db  
            else:
                return None  

        except Exception as ex:
            print(f"Error during login: {ex}")
            return None
