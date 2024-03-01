from app import db

class Roles_Permissions(db.Model):
    __tablename__ = 'roles_permissions'
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), primary_key=True)
    permission_id = db.Column(db.Integer, db.ForeignKey('permissions.id'), primary_key=True)

    def __init__(self,role_id, permission_id):
        self.role_id = role_id
        self.permission_id = permission_id