from flask import jsonify, make_response
from app.utils.jwt import encode_auth_token
from ..models.user import User
from .. import db

def create_stock(data):
    return jsonify({"message": "create_stock logged successfully"}), 200

def upload_stocks_file(file):
    return jsonify({"message": "upload_stocks_file logged successfully"}), 200

def get_all_stocks():
    return jsonify({"message": "get_all_stocks logged successfully"}), 200

def get_stock_by_company(company):
    return jsonify({"message": "get_stock_by_company logged successfully"}), 200

def get_stocks_by_date_range(start_date, end_date):
    return jsonify({"message": "get_stocks_by_date_range logged successfully"}), 200

def search_stocks(search_params):
    return jsonify({"message": "search_stocks logged successfully"}), 200

def compare_stocks(company_1, company_2, date_1, date_2):
    return jsonify({"message": "compare_stocks logged successfully"}), 200

def get_stock_stats(company, start_date, end_date):
    return jsonify({"message": "get_stock_stats logged successfully"}), 200

