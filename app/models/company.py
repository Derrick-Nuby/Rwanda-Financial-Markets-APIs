from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from .. import db

class Company(db.Model):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company_name = db.Column(db.String(30), nullable=False)
    ticker_symbol = db.Column(db.String(10), nullable=False)
    sector = db.Column(db.String(20), nullable=False)
    country = db.Column(db.String(20), nullable=False)
    market_cap = db.Column(db.Float, nullable=False)
    date_founded = db.Column(db.Date, nullable=False)
    date_traded = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    price = db.Column(db.Float, nullable=False)

    def __init__(self, company_name, ticker_symbol, sector, country, market_cap, date_founded, date_traded, price):
        self.company_name = company_name
        self.ticker_symbol = ticker_symbol
        self.sector = sector
        self.country = country
        self.market_cap = float(market_cap)
        self.date_founded = datetime.strptime(date_founded, '%Y-%m-%d').date()
        self.date_traded = datetime.strptime(date_traded, '%Y-%m-%d').date()
        self.price = float(price)

    def __repr__(self):
        return f'<Company {self.company_name} ({self.ticker_symbol})>'
