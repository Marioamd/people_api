from marshmallow import Schema, fields, validate, ValidationError
from Models.roles_model import Roles
from Models.permissions_model import Permissions

class RolePermissionSchema(Schema):
    role_id = fields.Int(required=True, validate=validate.Length(min=1))
    permission_id = fields.Int(required=True, validate=validate.Length(min=1))

    def validate_role_id(self, id):
        if not Roles.query.get(id):
            raise ValidationError("Role does not exist.")

    def validate_permission_id(self, id):
        if not Permissions.query.get(id):
            raise ValidationError("Permission does not exist.")


