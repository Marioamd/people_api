from flask import jsonify, request
from app import user_schema, users_schema, db
from Models.users_model import Users

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

    all_users = Users.query.all()
    result = users_schema.dump(all_users)

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

