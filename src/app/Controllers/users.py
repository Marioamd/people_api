from flask import jsonify, request
from app import user_schema, users_schema, db
from app.Models.users_model import Users

def create_user():
    
    errors = user_schema.validate(request.json)
    if errors:
        return jsonify({"errores": errors}), 400
    
    if len(request.json) > len(user_schema.fields):
        return jsonify({"error": "Additional fields are not allowed"}), 400
    
    new_user = Users(**request.json)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)


def get_users():

    active_users = request.args.get('active', '')
    
    if active_users == 'true':
        users = Users.query.filter_by(active=True).all()
    elif active_users == 'false':
        users = Users.query.filter_by(active=False).all()
    else:
        users = Users.query.all()
    
    if not users:
        return jsonify({'message': 'Users not found!'}), 404

    result = users_schema.dump(users)

    return jsonify(result)


def get_user(id):
    
    user = Users.query.get(id)

    return user_schema.jsonify(user)


def update_user(id):
    user = Users.query.get(id)

    if not user:
        return jsonify({'message': 'User Not found'}),404
    
    for key, value in request.json.items():
        if hasattr(user, key):
            setattr(user, key, value)

    db.session.commit()

    return user_schema.jsonify(user)


def delete_user(id):
    user = Users.query.get(id)
    
    if not user:
        return jsonify({'message': 'User Not found'}),404
    
    user.active = False
    db.session.commit()
    
    return user_schema.jsonify(user)

