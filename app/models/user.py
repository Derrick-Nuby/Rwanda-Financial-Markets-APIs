from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    has_verified_email_address = db.Column(db.Boolean, default=False)
    phone_number = db.Column(db.String(20), unique=True, nullable=True)
    has_verified_phone_number = db.Column(db.Boolean, default=False)
    password = db.Column(db.String(128), nullable=False)  # Store hashed password
    image_url = db.Column(db.String(255), nullable=True)
    country = db.Column(db.String(50), nullable=True)
    banned = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, first_name, last_name, username, email, password, phone_number=None, image_url=None, country=None):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.set_password(password)
        self.phone_number = phone_number
        self.image_url = image_url
        self.country = country

    def set_password(self, password):
        """Hashes the password and stores it."""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Verifies if the provided password matches the stored hash."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.username}>'
