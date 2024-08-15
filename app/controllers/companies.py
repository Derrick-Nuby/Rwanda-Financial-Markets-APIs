from flask import jsonify
from ..models.company import Company
from .. import db

def create_company(data):
    required_fields = ['company_name', 'ticker_symbol', 'sector', 'country', 'market_cap', 'date_founded',
'date_traded' ]
    
    for field in required_fields:
        if field not in data:
            return jsonify({"message": f"Missing {field}"}), 400
    try:
        company = Company(
            company_name=data['company_name'],
            ticker_symbol=data['ticker_symbol'],
            sector=data['sector'],
            country=data['country'],
            market_cap=data['market_cap'],
            date_founded=data['date_founded'],
            date_traded=data['date_traded'],
            price=data['price']
        )
        db.session.add(company)
        db.session.commit()
        return jsonify({"message": "Company created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 400

def get_all_companies():
    companies = Company.query.all()
    return jsonify([company.as_dict() for company in companies]), 200

def get_company_by_ticker(ticker):
    company = Company.query.filter_by(ticker_symbol=ticker).first()
    if company:
        return jsonify(company.as_dict()), 200
    return jsonify({"message": "Company not found"}), 404

def update_company(ticker, data):
    company = Company.query.filter_by(ticker_symbol=ticker).first()
    if company:
        for key, value in data.items():
            setattr(company, key, value)
        db.session.commit()
        return jsonify({"message": "Company updated successfully"}), 200
    return jsonify({"message": "Company not found"}), 404

def delete_company(ticker):
    company = Company.query.filter_by(ticker_symbol=ticker).first()
    if company:
        db.session.delete(company)
        db.session.commit()
        return jsonify({"message": "Company deleted successfully"}), 200
    return jsonify({"message": "Company not found"}), 404

def get_best_performing_company():
    company = Company.query.order_by(Company.price.desc()).first()
    if company:
        return jsonify(company.as_dict()), 200
    return jsonify({"message": "No companies found"}), 404

def get_worst_performing_company():
    company = Company.query.order_by(Company.price.asc()).first()
    if company:
        return jsonify(company.as_dict()), 200
    return jsonify({"message": "No companies found"}), 404

def search_companies(search_params):
    query = Company.query
    for key, value in search_params.items():
        query = query.filter(getattr(Company, key).like(f"%{value}%"))
    companies = query.all()
    return jsonify([company.as_dict() for company in companies]), 200

def as_dict(self):
    return {
        "id": self.id,
        "company_name": self.company_name,
        "ticker_symbol": self.ticker_symbol,
        "sector": self.sector,
        "country": self.country,
        "market_cap": self.market_cap,
        "date_founded": self.date_founded.isoformat(),
        "date_traded": self.date_traded.isoformat(),
        "price": self.price,
        "created_at": self.created_at.isoformat()
    }

Company.as_dict = as_dict
