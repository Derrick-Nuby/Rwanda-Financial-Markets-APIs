from flask import jsonify, make_response
from datetime import datetime
from ..models.stocks import Stocks
from .. import db

def create_stock(data):
    try:
        new_stock = Stocks(
            company=data['company'],
            date=data['date'],
            price=data['price']
        )
        db.session.add(new_stock)
        db.session.commit()
        return make_response(jsonify({"message": "Stock created successfully"}), 201)
    except Exception as e:
        return make_response(jsonify({"message": str(e)}), 400)

def upload_stocks_file(file):
    return jsonify({"message": "upload_stocks_file logged successfully"}), 200

def get_all_stocks():
    try:
        stocks = Stocks.query.all()
        result = [
            {
                "id": stock.id,
                "company": stock.company,
                "date": stock.date.strftime('%Y-%m-%d'),
                "price": stock.price,
                "created_at": stock.created_at.strftime('%Y-%m-%d %H:%M:%S')
            }
            for stock in stocks
        ]
        return jsonify(result), 200
    except Exception as e:
        return make_response(jsonify({"message": str(e)}), 400)

def get_stock_by_company(company):
    try:
        stocks = Stocks.query.filter_by(company=company).all()
        if not stocks:
            return make_response(jsonify({"message": "No stocks found for this company"}), 404)
        
        result = [
            {
                "id": stock.id,
                "company": stock.company,
                "date": stock.date.strftime('%Y-%m-%d'),
                "price": stock.price,
                "created_at": stock.created_at.strftime('%Y-%m-%d %H:%M:%S')
            }
            for stock in stocks
        ]
        return jsonify(result), 200
    except Exception as e:
        return make_response(jsonify({"message": str(e)}), 400)

def get_stocks_by_date_range(start_date, end_date):
    try:
        stocks = Stocks.query.filter(Stocks.date.between(start_date, end_date)).all()
        result = [
            {
                "id": stock.id,
                "company": stock.company,
                "date": stock.date.strftime('%Y-%m-%d'),
                "price": stock.price,
                "created_at": stock.created_at.strftime('%Y-%m-%d %H:%M:%S')
            }
            for stock in stocks
        ]
        return jsonify(result), 200
    except Exception as e:
        return make_response(jsonify({"message": str(e)}), 400)

def search_stocks(search_params):
    try:
        query = Stocks.query
        if 'company' in search_params:
            query = query.filter_by(company=search_params['company'])
        if 'date' in search_params:
            query = query.filter_by(date=datetime.strptime(search_params['date'], '%Y-%m-%d').date())
        if 'price' in search_params:
            query = query.filter_by(price=float(search_params['price']))

        stocks = query.all()
        result = [
            {
                "id": stock.id,
                "company": stock.company,
                "date": stock.date.strftime('%Y-%m-%d'),
                "price": stock.price,
                "created_at": stock.created_at.strftime('%Y-%m-%d %H:%M:%S')
            }
            for stock in stocks
        ]
        return jsonify(result), 200
    except Exception as e:
        return make_response(jsonify({"message": str(e)}), 400)

def compare_stocks(company_1, company_2, date_1, date_2):
    try:
        stock_1 = Stocks.query.filter_by(company=company_1, date=date_1).first()
        stock_2 = Stocks.query.filter_by(company=company_2, date=date_2).first()
        if not stock_1 or not stock_2:
            return make_response(jsonify({"message": "One or both stocks not found"}), 404)
        
        comparison = {
            "company_1": {
                "company": stock_1.company,
                "date": stock_1.date.strftime('%Y-%m-%d'),
                "price": stock_1.price
            },
            "company_2": {
                "company": stock_2.company,
                "date": stock_2.date.strftime('%Y-%m-%d'),
                "price": stock_2.price
            },
            "price_difference": abs(stock_1.price - stock_2.price)
        }
        return jsonify(comparison), 200
    except Exception as e:
        return make_response(jsonify({"message": str(e)}), 400)

def get_stock_stats(company, start_date, end_date):
    try:
        stocks = Stocks.query.filter(
            Stocks.company == company,
            Stocks.date.between(start_date, end_date)
        ).all()

        if not stocks:
            return make_response(jsonify({"message": "No stocks found for the given criteria"}), 404)
        
        highest_price = max(stocks, key=lambda x: x.price)
        lowest_price = min(stocks, key=lambda x: x.price)
        average_price = sum(stock.price for stock in stocks) / len(stocks)

        stats = {
            "highest_price": {
                "date": highest_price.date.strftime('%Y-%m-%d'),
                "price": highest_price.price
            },
            "lowest_price": {
                "date": lowest_price.date.strftime('%Y-%m-%d'),
                "price": lowest_price.price
            },
            "average_price": average_price
        }
        return jsonify(stats), 200
    except Exception as e:
        return make_response(jsonify({"message": str(e)}), 400)
