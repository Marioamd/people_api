from flask import jsonify, request
from app import role_permission_schema, roles_permissions_schema, db
from app.Models.roles_permissions_model import Roles_Permissions

def create_role_permission():
    
    errors = role_permission_schema.validate(request.json)
    if errors:
        return jsonify({"errores": errors}), 400
    
    if len(request.json) > len(role_permission_schema.fields):
        return jsonify({"error": "Additional fields are not allowed"}), 400
    
    new_role_permission = Roles_Permissions(**request.json)

    db.session.add(new_role_permission)
    db.session.commit()

    return role_permission_schema.jsonify(new_role_permission)


def get_roles_permissions():

    all_roles_permissions = Roles_Permissions.query.all()
    result = roles_permissions_schema.dump(all_roles_permissions)

    return jsonify(result)


def get_role_permission(role_id):
    
    roles_permissions = Roles_Permissions.query.filter_by(role_id=role_id).all()
    result = roles_permissions_schema.dump(roles_permissions)

    return jsonify(result)



def update_role_permission(role_id, permission_id):
    
    existing_role_permission = Roles_Permissions.query.filter_by(role_id=role_id, permission_id=permission_id).first()

    if not existing_role_permission:
        return jsonify({'message': 'Role-Permission Not found'}),404
    
    existing_role_permission.role_id= request.json.get('role_id', existing_role_permission.role_id)
    existing_role_permission.permission_id= request.json.get('permission_id', existing_role_permission.permission_id)

    db.session.commit()

    return role_permission_schema.jsonify(existing_role_permission)


def delete_role_permission(role_id, permission_id):
    
    role_permission = Roles_Permissions.query.get(role_id, permission_id)

    if not role_permission:
        return jsonify({'message': 'Role or Permission Not found'}),404
  
    role_permission.active = False
    db.session.commit()

    return role_permission_schema.jsonify(role_permission)