from marshmallow import Schema, fields, validate, ValidationError
from app.Models.roles_model import Roles
from app.Models.permissions_model import Permissions

class RolePermissionSchema(Schema):
    role_id = fields.Int(required=True, validate=validate.Range(min=1))
    permission_id = fields.Int(required=True, validate=validate.Range(min=1))

    def validate_role_id(self, role_id):
        if not Roles.query.get(role_id):
            raise ValidationError("Role does not exist.")

    def validate_permission_id(self, permission_id):
        if not Permissions.query.get(permission_id):
            raise ValidationError("Permission does not exist.")


