from flask import jsonify, make_response
from app.utils.jwt import encode_auth_token
from ..models.user import User
from .. import db

def register_user(data):
    required_fields = ['first_name', 'last_name', 'username', 'email', 'password', 'phone_number', 'country']
    
    for field in required_fields:
        if field not in data:
            return jsonify({"message": f"Missing {field}"}), 400
    
    user = User(
        first_name=data['first_name'],
        last_name=data['last_name'],
        username=data['username'],
        email=data['email'],
        password=data['password'],
        phone_number=data.get('phone_number'),
        image_url=data.get('image_url'),
        country=data.get('country')
    )
    
    try:
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 500

def get_single_user(user_id: int):
    user = User.query.get_or_404(user_id)
    
    if user:
        return jsonify({
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "email": user.email,
            "phone_number": user.phone_number,
            "image_url": user.image_url,
            "country": user.country
        }), 200
    return jsonify({"message": "User not found"}), 404

def update_user(user_id: int, data):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    for key, value in data.items():
        if hasattr(user, key):
            setattr(user, key, value)

    try:
        db.session.commit()
        return jsonify({"message": "User updated successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 500

def delete_user(user_id: int):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    try:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 500

def login_user(data):
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"message": "Missing fields"}), 400

    user = User.query.filter_by(email=email).first()

    if not user or not user.check_password(password):
        return jsonify({"message": "Invalid email or password"}), 401

    token = encode_auth_token(user.id, user.email)
    
    response = make_response(jsonify({"message": "Login successful"}))
    
    response.set_cookie(
        'jwt',
        value=token,
        httponly=True,
        secure=True,
        samesite='Lax',
        max_age=60*60*24
    )

    return response, 200

def get_all_users():
    users = User.query.all()
    users_list = [{
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "username": user.username,
        "email": user.email,
        "phone_number": user.phone_number,
        "image_url": user.image_url,
        "country": user.country
    } for user in users]
    return jsonify(users_list), 200

def logout_user():
    return jsonify({"message": "logout_user logged successfully"}), 200

def get_logged_in_user():
    return jsonify({"message": "get_logged_in_user logged successfully"}), 200

