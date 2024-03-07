from flask import jsonify, request
from app import role_schema, roles_schema, db
from Models.roles_model import Roles

def create_role():
    
    errors = role_schema.validate(request.json)
    if errors:
        return jsonify({"errores": errors}), 400
    
    if len(request.json) > len(role_schema.fields):
        return jsonify({"error": "Additional fields are not allowed"}), 400
    
    new_role = Roles(**request.json)

    db.session.add(new_role)
    db.session.commit()

    return role_schema.jsonify(new_role)


def get_roles():

    active_roles = request.args.get('active', '')
    
    if active_roles == 'true':
        roles = Roles.query.filter_by(active=True).all()
    elif active_roles == 'false':
        roles = Roles.query.filter_by(active=False).all()
    else:
        roles = Roles.query.all()
    
    if not roles:
        return jsonify({'message': 'Roles not found!'}), 404

    result = roles_schema.dump(active_roles)

    return jsonify(result)


def get_role(id):
    
    role = Roles.query.get(id)

    return role_schema.jsonify(role)


def update_role(id):
    role = Roles.query.get(id)

    if not role:
        return jsonify({'message': 'Role Not found'}),404
    
    for key, value in request.json.items():
        if hasattr(role, key):
            setattr(role, key, value)

    db.session.commit()

    return role_schema.jsonify(role)


def delete_role(id):
    role = Roles.query.get(id)

    if not role:
        return jsonify({'message': 'Role Not found'}),404
  
    role.active = False
    db.session.commit()

    return role_schema.jsonify(role)