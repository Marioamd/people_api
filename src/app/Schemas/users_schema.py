from marshmallow import Schema, fields, validate, ValidationError
from app.Models.roles_model import Roles

class UserSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1))
    lastname = fields.Str(required=True, validate=validate.Length(min=1))
    dni = fields.Str(required=True, validate=[validate.Length(min=1), validate.Length(max=10)])
    role_id = fields.Int(required=True, validate=validate.Range(min=1))
    email = fields.Str(required=True, validate=validate.Length(min=1))
    password = fields.Str(required=True, validate=validate.Length(min=1))
    avatar_url= fields.Str(allow_none=True)
    country= fields.Str(allow_none=True)
    city= fields.Str(allow_none=True)
    address= fields.Str(allow_none=True)
    phone_prefix = fields.Str(allow_none=True)
    phone_number = fields.Str(allow_none=True)
   
    def validate_role_id(self, role_id):
        if not Roles.query.get(role_id):
            raise ValidationError("Role does not exist.")
