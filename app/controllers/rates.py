from flask import jsonify, make_response
from ..models.rates import Rates
from .. import db

def create_rate(data):
    try:
        new_rate = Rates(
            country=data['country'],
            code=data['code'],
            date=data['date'],
            buying_value=data['buying_value'],
            average_value=data['average_value'],
            selling_value=data['selling_value']
        )
        db.session.add(new_rate)
        db.session.commit()
        return jsonify({"message": "Rate created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

def upload_rates_file(file):
    return jsonify({"message": "Rates uploaded successfully"}), 200

def get_all_rates():
    try:
        rates = Rates.query.all()
        result = [rate.to_dict() for rate in rates]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

def get_rates_by_country(country):
    try:
        rates = Rates.query.filter_by(country=country).all()
        result = [rate.to_dict() for rate in rates]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

def get_rates_by_date_range(start_date, end_date):
    try:
        rates = Rates.query.filter(Rates.date.between(start_date, end_date)).all()
        result = [rate.to_dict() for rate in rates]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

def search_rates(search_params):
    query = Rates.query
    for key, value in search_params.items():
        query = query.filter(getattr(Rates, key).like(f"%{value}%"))
    rates = query.all()
    return jsonify([rate.to_dict() for rate in rates]), 200

def compare_rates(currency_1, currency_2, date_1, date_2):
    try:
        rate_1 = Rates.query.filter_by(code=currency_1, date=date_1).first()
        rate_2 = Rates.query.filter_by(code=currency_2, date=date_2).first()

        if not rate_1 or not rate_2:
            return jsonify({"error": "One or both rates not found"}), 404

        comparison = {
            currency_1: {
                "buying_value": rate_1.buying_value,
                "average_value": rate_1.average_value,
                "selling_value": rate_1.selling_value,
            },
            currency_2: {
                "buying_value": rate_2.buying_value,
                "average_value": rate_2.average_value,
                "selling_value": rate_2.selling_value,
            }
        }

        return jsonify(comparison), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

def get_rate_stats(currency, start_date, end_date):
    try:
        rates = Rates.query.filter_by(code=currency).filter(Rates.date.between(start_date, end_date)).all()

        if not rates:
            return jsonify({"error": "No rates found for the specified period"}), 404

        total_rates = len(rates)
        avg_buying_value = sum(rate.buying_value for rate in rates) / total_rates
        avg_selling_value = sum(rate.selling_value for rate in rates) / total_rates
        avg_average_value = sum(rate.average_value for rate in rates) / total_rates

        stats = {
            "currency": currency,
            "total_rates": total_rates,
            "avg_buying_value": avg_buying_value,
            "avg_selling_value": avg_selling_value,
            "avg_average_value": avg_average_value,
        }

        return jsonify(stats), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

def get_all_currencies():
    try:
        currencies = db.session.query(Rates.code).distinct().all()
        result = [currency[0] for currency in currencies]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

def get_all_countries():
    try:
        countries = db.session.query(Rates.country).distinct().all()
        result = [country[0] for country in countries]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
    
def to_dict(self):
    return {
        "id": self.id,
        "country": self.country,
        "code": self.code,
        "date": self.date,
        "buying_value": self.buying_value,
        "average_value": self.average_value,
        "selling_value": self.selling_value,
        "created_at": self.created_at.isoformat()
    }

Rates.to_dict = to_dict
