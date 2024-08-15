from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    
    with app.app_context():
        from .routes.user import init_routes as init_user_routes
        from .routes.rates import init_routes as init_rates_routes
        from .routes.stocks import init_routes as init_stocks_routes
        from .routes.companies import init_routes as init_companies_routes
        
        init_user_routes(app)
        init_rates_routes(app)
        init_stocks_routes(app)
        init_companies_routes(app)
        db.create_all()
    
    return app