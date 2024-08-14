from flask import request
from ..controllers import user as user_controller

def init_routes(app):
    
    @app.route("/user", methods=["POST"])
    def register_user():
        data = request.get_json()
        return user_controller.register_user(data)
    
    @app.route("/user/<int:id>", methods=["GET"])
    def get_single_user(id: int):
        return user_controller.get_single_user(id)
    
    @app.route("/user/<int:id>", methods=["PUT"])
    def update_user(id: int):
        data = request.get_json()
        return user_controller.update_user(id, data)
    
    @app.route("/user/<int:id>", methods=["DELETE"])
    def delete_user(id: int):
        return user_controller.delete_user(id)
    
    @app.route("/login", methods=["POST"])
    def login_user():
        data = request.get_json()
        return user_controller.login_user(data)
    
    @app.route("/user/all", methods=["GET"])
    def get_all_users():
        return user_controller.get_all_users()
    
    @app.route("/logout", methods=["GET"])
    def logout_user():
        return user_controller.logout_user()
    
    @app.route("/user/in", methods=["GET"])
    def get_logged_in_user():
        return user_controller.get_logged_in_user()
    
    