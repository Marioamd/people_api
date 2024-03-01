from app import db

class Permissions(db.Model):
    __tablename__ = 'permissions'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    description = db.Column(db.String(150), nullable=False)

    def __init__(self,description):
        self.description = description