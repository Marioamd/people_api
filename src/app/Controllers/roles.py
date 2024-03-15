from flask import jsonify, request
from app import role_schema, roles_schema, db
from app.Models.roles_model import Roles


def create_role():
    
    errors = role_schema.validate(request.json)
    if errors:
        return jsonify({"errors": errors}), 400
            
    role_data = role_schema.load(request.json)
    new_role = Roles(**role_data)

    db.session.add(new_role)
    db.session.commit()

    result = role_schema.dump(new_role)
    return jsonify(result), 201 
        

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

    result = roles_schema.dump(roles)
    return jsonify(result)


def get_role(id):
    role = Roles.query.get(id)

    if not role:
        return jsonify({'message': 'Role Not found'}), 404

    result = role_schema.dump(role)
    return jsonify(result)


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