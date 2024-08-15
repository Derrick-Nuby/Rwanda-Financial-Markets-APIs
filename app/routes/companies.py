from flask import request
from ..controllers import companies as companies_controller

def init_routes(app):
    
    @app.route("/companies", methods=["POST"])
    def create_company():
        data = request.get_json()
        return companies_controller.create_company(data)
    
    @app.route("/companies", methods=["GET"])
    def get_all_companies():
        return companies_controller.get_all_companies()
    
    @app.route("/companies/<string:ticker>", methods=["GET"])
    def get_company_by_ticker(ticker):
        return companies_controller.get_company_by_ticker(ticker)
    
    @app.route("/companies/<string:ticker>", methods=["PUT"])
    def update_company(ticker):
        data = request.get_json()
        return companies_controller.update_company(ticker, data)
    
    @app.route("/companies/<string:ticker>", methods=["DELETE"])
    def delete_company(ticker):
        return companies_controller.delete_company(ticker)
    
    @app.route("/companies/best", methods=["GET"])
    def get_best_performing_company():
        return companies_controller.get_best_performing_company()
    
    @app.route("/companies/worst", methods=["GET"])
    def get_worst_performing_company():
        return companies_controller.get_worst_performing_company()
    
    @app.route("/companies/search", methods=["GET"])
    def search_companies():
        search_params = request.args.to_dict()
        return companies_controller.search_companies(search_params)
