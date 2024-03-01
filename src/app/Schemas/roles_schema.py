from marshmallow import Schema, fields, validate

class RoleSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1))