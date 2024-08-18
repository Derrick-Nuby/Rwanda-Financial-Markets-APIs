from flask import jsonify, make_response
from app.utils.jwt import encode_auth_token
from sqlalchemy.exc import SQLAlchemyError
from ..models.user import User
from .. import db

def validate_required_fields(data, required_fields):
    for field in required_fields:
        if field not in data:
            return jsonify({"message": f"Missing {field}"}), 400
    return None


def register_user(data):
    required_fields = ['first_name', 'last_name', 'username', 'email', 'password', 'phone_number', 'country']
    
    validation_error = validate_required_fields(data, required_fields)
    if validation_error:
        return validation_error

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
        return jsonify({"message": "User registered successfully", "user": user.as_dict()}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 500

def get_single_user(user_id: int):
    user = User.query.get_or_404(user_id)
    return jsonify(user.as_dict()), 200

def update_user(user_id: int, data):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    for key, value in data.items():
        if hasattr(user, key):
            setattr(user, key, value)

    try:
        db.session.commit()
        return jsonify({"message": "User updated successfully", "user": user.as_dict()}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"message": "Database error occurred"}), 500
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 500

def delete_user(user_id: int):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    try:
        deleted_user_data = user.as_dict()
        
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully", "user": deleted_user_data}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"message": "Database error occurred"}), 500
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 500

def login_user(data):
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"message": "Missing email or password"}), 400

    user = User.query.filter_by(email=email).first()

    if not user or not user.check_password(password):
        return jsonify({"message": "Invalid email or password"}), 401

    token = encode_auth_token(user.id, user.email)
    
    response = make_response(jsonify({"message": "Login successful", "user": user.as_dict()}))
    
    response.set_cookie(
        'jwt',
        value=token,
        httponly=True,
        secure=True,
        samesite='Lax',
        max_age=60*60*24  # 1 day
    )

    return response, 200

def get_all_users():
    users = User.query.all()
    users_list = [user.as_dict() for user in users]
    total_users = len(users_list)
    return jsonify({"total":total_users, "users": users_list}), 200

def logout_user():
    return jsonify({"message": "Logout successful"}), 200

def get_logged_in_user():
    return jsonify({"message": "Logged-in user data"}), 200
