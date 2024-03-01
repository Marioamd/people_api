from marshmallow import Schema, fields, validate

class PermissionSchema(Schema):
    description = fields.Str(required=True, validate=validate.Length(min=1))