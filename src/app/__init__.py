from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.getenv("SECRET_KEY")
jwt_key = os.getenv("JWT_KEY")

db = SQLAlchemy(app)
ma = Marshmallow(app)

from .Schemas.users_schema import UserSchema
from .Schemas.roles_schema import RoleSchema
from .Schemas.permissions_schema import PermissionSchema
from .Schemas.roles_permissions_schema import RolePermissionSchema


user_schema = UserSchema()
users_schema = UserSchema(many=True)


role_schema = RoleSchema()
roles_schema = RoleSchema(many=True)


permission_schema = PermissionSchema()
permissions_schema = PermissionSchema(many=True)


role_permission_schema = RolePermissionSchema()
roles_permissions_schema = RolePermissionSchema(many=True)


from .Routes import users_routes
from .Routes import roles_routes
from .Routes import roles_permissions_routes
from .Routes import permissions_routes
from .Routes import login_route