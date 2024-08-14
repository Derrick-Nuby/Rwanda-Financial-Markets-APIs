from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from .. import db

class Stocks(db.Model):
    __tablename__ = 'stocks'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(20), unique=True, nullable=False)
    price = db.Column(db.String(30), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, company, date, price):
        self.company = company
        self.date = date
        self.price = price

    def __repr__(self):
        return f'<User {self.date}>'
