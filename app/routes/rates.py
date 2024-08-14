from flask import request
from ..controllers import rates as rates_controller

def init_routes(app):
    
    @app.route("/rates", methods=["POST"])
    def create_rate():
        data = request.get_json()
        return rates_controller.create_rate(data)
    
    @app.route("/rates/file", methods=["POST"])
    def upload_rates_file():
        file = request.files['file']
        return rates_controller.upload_rates_file(file)
    
    @app.route("/rates", methods=["GET"])
    def get_all_rates():
        return rates_controller.get_all_rates()
    
    @app.route("/rates/country/<string:country>", methods=["GET"])
    def get_rates_by_country(country: str):
        return rates_controller.get_rates_by_country(country)
    
    @app.route("/rates/date-range", methods=["GET"])
    def get_rates_by_date_range():
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        return rates_controller.get_rates_by_date_range(start_date, end_date)
    
    @app.route("/rates/search", methods=["GET"])
    def search_rates():
        search_params = request.args.to_dict()
        return rates_controller.search_rates(search_params)
    
    @app.route("/rates/compare", methods=["GET"])
    def compare_rates():
        currency_1 = request.args.get('currency_1')
        currency_2 = request.args.get('currency_2')
        date_1 = request.args.get('date_1')
        date_2 = request.args.get('date_2')
        return rates_controller.compare_rates(currency_1, currency_2, date_1, date_2)
    
    @app.route("/rates/stats", methods=["GET"])
    def get_rate_stats():
        currency = request.args.get('currency')
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        return rates_controller.get_rate_stats(currency, start_date, end_date)
    
    @app.route("/rates/currencies", methods=["GET"])
    def get_all_currencies():
        return rates_controller.get_all_currencies()
    
    @app.route("/rates/countries", methods=["GET"])
    def get_all_countries():
        return rates_controller.get_all_countries()
