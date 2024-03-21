from flask import jsonify, request
from app import user_schema, users_schema, db
from app.Models.users_model import Users
from app.Services.security import Security

def create_user():
    
    errors = user_schema.validate(request.json)
    if errors:
        return jsonify({"errores": errors}), 400
    
    if len(request.json) > len(user_schema.fields):
        return jsonify({"error": "Additional fields are not allowed"}), 400

    user_data = user_schema.load(request.json)

    hashed_password = Security.hash_password(user_data['password'])
    user_data['password'] = hashed_password
    
    new_user = Users(**user_data)

    db.session.add(new_user)
    db.session.commit()

    result = user_schema.dump(new_user)
    return jsonify(result)


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

    return jsonify(users_schema.dump(users))


def get_user(id):
    
    user = Users.query.get(id)

    if not user:
        return jsonify({'message': 'User not found!'}), 404
    
    result = user_schema.dump(user)

    return jsonify(result)


def update_user(id):
    user = Users.query.get(id)

    if not user:
        return jsonify({'message': 'User Not found'}),404
    
    for key, value in request.json.items():
        if hasattr(user, key):
            setattr(user, key, value)

    db.session.commit()
    result = user_schema.dump(user)

    return jsonify(result)


def delete_user(id):
    user = Users.query.get(id)
    
    if not user:
        return jsonify({'message': 'User Not found'}),404
    
    user.active = False
    db.session.commit()
    
    return jsonify({'message': 'User deactivated successfully'})


