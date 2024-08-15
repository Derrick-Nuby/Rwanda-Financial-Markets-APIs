from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from .. import db

class Rates(db.Model):
    __tablename__ = 'rates'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country = db.Column(db.String(20), nullable=False)
    code = db.Column(db.String(10), nullable=False)
    date = db.Column(db.Date, nullable=False)
    buying_value = db.Column(db.Float, nullable=False)
    average_value = db.Column(db.Float, nullable=False)
    selling_value = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, country, code, date, buying_value, average_value, selling_value):
        self.country = country
        self.code = code
        self.date = datetime.strptime(date, '%Y-%m-%d').date()
        self.buying_value = float(buying_value)
        self.average_value = float(average_value)
        self.selling_value = float(selling_value)


    def __repr__(self):
        return f'<Rates {self.date}>'
