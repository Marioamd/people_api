from app import db

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30),nullable=False)
    dni = db.Column(db.String(10),nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'),nullable=False)
    email = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(255), nullable=False)
    avatar_url = db.Column(db.String(255),nullable=True)
    country = db.Column(db.String(20),nullable=True)
    city = db.Column(db.String(20),nullable=True)
    address = db.Column(db.String(50),nullable=True)
    phone_prefix = db.Column(db.String(10),nullable=True)
    phone_number = db.Column(db.String(20),nullable=True)
    
    active = db.Column(db.Boolean, default=True)

    def __init__(self,name,lastname,dni,role_id,email,password,avatar_url,country,city,address,phone_prefix,phone_number):
        self.name = name
        self.lastname = lastname
        self.dni = dni
        self.role_id = role_id
        self.email = email
        self.password = password
        self.avatar_url = avatar_url
        self.country = country
        self.city = city
        self.address = address
        self.phone_prefix = phone_prefix
        self.phone_number = phone_number