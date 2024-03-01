from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root@localhost/peoplemicroservice'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

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


