import jwt
import datetime
from flask import current_app

def encode_auth_token(user_id, email):
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow(),
            'user_id': user_id,
            'email': email
        }
        token = jwt.encode(payload, current_app.config.get('SECRET_KEY'), algorithm='HS256')
        
        return token
    except Exception as e:
        return str(e)
