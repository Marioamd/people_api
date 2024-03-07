from app import db

class Permissions(db.Model):
    __tablename__ = 'permissions'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    description = db.Column(db.String(150), nullable=False)

    active = db.Column(db.Boolean, default=True)
    
    def __init__(self,description):
        self.description = description