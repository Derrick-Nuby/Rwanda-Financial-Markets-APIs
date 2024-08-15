from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from .. import db

class Stocks(db.Model):
    __tablename__ = 'stocks'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company = db.Column(db.String(20), nullable=False)
    date = db.Column(db.Date, nullable=False)
    price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, company, date, price):
        self.company = company
        self.date = datetime.strptime(date, '%Y-%m-%d').date()
        self.price = float(price)

    def __repr__(self):
        return f'<Stock {self.company} on {self.date}: ${self.price}>'
