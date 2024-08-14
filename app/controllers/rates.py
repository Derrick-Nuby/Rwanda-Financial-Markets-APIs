from flask import jsonify, make_response
from app.utils.jwt import encode_auth_token
from ..models.user import User
from .. import db

def create_rate(data):
    return jsonify({"message": "create_rate logged successfully"}), 200

def upload_rates_file(file):
    return jsonify({"message": "upload_rates_file logged successfully"}), 200

def get_all_rates():
    return jsonify({"message": "get_all_rates logged successfully"}), 200

def get_rates_by_country(country):
    return jsonify({"message": "get_rates_by_country logged successfully"}), 200

def get_rates_by_date_range(start_date, end_date):
    return jsonify({"message": "get_rates_by_date_range logged successfully"}), 200

def search_rates(search_params):
    return jsonify({"message": "search_rates logged successfully"}), 200

def compare_rates(currency_1, currency_2, date_1, date_2):
    return jsonify({"message": "compare_rates logged successfully"}), 200

def get_rate_stats(currency, start_date, end_date):
    return jsonify({"message": "get_rate_stats logged successfully"}), 200

def get_all_currencies():
    return jsonify({"message": "get_all_currencies logged successfully"}), 200

def get_all_countries():
    return jsonify({"message": "get_all_countries logged successfully"}), 200

