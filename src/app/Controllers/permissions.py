from flask import jsonify, request
from app import permission_schema, permissions_schema, db
from Models.permissions_model import Permissions

def create_permission():
    
    errors = permission_schema.validate(request.json)
    if errors:
        return jsonify({"errores": errors}), 400
    
    if len(request.json) > len(permission_schema.fields):
        return jsonify({"error": "Additional fields are not allowed"}), 400
    
    new_permission = Permissions(**request.json)

    db.session.add(new_permission)
    db.session.commit()

    return permission_schema.jsonify(new_permission)


def get_permissions():

    active_permissions = request.args.get('active', '')
    
    if active_permissions == 'true':
        permissions = Permissions.query.filter_by(active=True).all()
    elif active_permissions == 'false':
        permissions = Permissions.query.filter_by(active=False).all()
    else:
        permissions = Permissions.query.all()
    
    if not permissions:
        return jsonify({'message': 'Permissions not found!'}), 404
    
    result = permissions_schema.dump(active_permissions)

    return jsonify(result)


def get_permission(id):
    
    permission = Permissions.query.get(id)

    return permission_schema.jsonify(permission)


def update_permission(id):
    permission = Permissions.query.get(id)

    if not permission:
        return jsonify({'message': 'Permission Not found'}),404
    
    for key, value in request.json.items():
        if hasattr(permission, key):
            setattr(permission, key, value)

    db.session.commit()

    return permission_schema.jsonify(permission)


def delete_permission(id):
    
    permission = Permissions.query.get(id)

    if not permission:
        return jsonify({'message': 'Permission Not found'}),404
  
    permission.active = False
    db.session.commit()

    return permission_schema.jsonify(permission)