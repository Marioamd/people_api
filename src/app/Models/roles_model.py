from app import db
from .roles_permissions_model import Roles_Permissions

class Roles(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(30), nullable=False)

    active = db.Column(db.Boolean, default=True)

    users = db.relationship('users', backref='role', lazy=True)
    permissions = db.relationship('permissions', secondary=Roles_Permissions, backref=db.backref('roles', lazy=True))
    

    def __init__(self,name):
        self.name = name