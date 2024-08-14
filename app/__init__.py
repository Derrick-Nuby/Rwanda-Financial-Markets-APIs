from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    
    with app.app_context():
        from .routes.user import init_routes
        from .routes.rates import init_routes
        init_routes(app)
        db.create_all()
    
    return app