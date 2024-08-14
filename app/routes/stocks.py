from flask import request
from ..controllers import stocks as stocks_controller

def init_routes(app):
    
    @app.route("/stocks", methods=["POST"])
    def create_stock():
        data = request.get_json()
        return stocks_controller.create_stock(data)
    
    @app.route("/stocks/file", methods=["POST"])
    def upload_stocks_file():
        file = request.files['file']
        return stocks_controller.upload_stocks_file(file)
    
    @app.route("/stocks", methods=["GET"])
    def get_all_stocks():
        return stocks_controller.get_all_stocks()
    
    @app.route("/stocks/<string:company>", methods=["GET"])
    def get_stock_by_company(company: str):
        return stocks_controller.get_stock_by_company(company)
    
    @app.route("/stocks/date-range", methods=["GET"])
    def get_stocks_by_date_range():
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        return stocks_controller.get_stocks_by_date_range(start_date, end_date)
    
    @app.route("/stocks/search", methods=["GET"])
    def search_stocks():
        search_params = request.args.to_dict()
        return stocks_controller.search_stocks(search_params)
    
    @app.route("/stocks/compare", methods=["GET"])
    def compare_stocks():
        company_1 = request.args.get('company_1')
        company_2 = request.args.get('company_2')
        date_1 = request.args.get('date_1')
        date_2 = request.args.get('date_2')
        return stocks_controller.compare_stocks(company_1, company_2, date_1, date_2)
    
    @app.route("/stocks/stats", methods=["GET"])
    def get_stock_stats():
        company = request.args.get('company')
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        return stocks_controller.get_stock_stats(company, start_date, end_date)
