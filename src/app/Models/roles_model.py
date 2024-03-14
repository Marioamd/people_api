from app import db
from app.Models.roles_permissions_model import Roles_Permissions

class Roles(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(30), nullable=False)

    active = db.Column(db.Boolean, default=True)

    users = db.relationship('Users', backref='role', lazy=True)
    permissions = db.relationship('Permissions', secondary='roles_permissions', backref=db.backref('roles', lazy=True))
    

    def __init__(self,name):
        self.name = name