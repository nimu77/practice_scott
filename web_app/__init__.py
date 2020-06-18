from flask import Flask
from web_app.routes.home_routes import home_routes
from web_app.routes.apitest_routes import apitest_routes

def create_app():
    app = Flask(__name__)

    app.register_blueprint(home_routes)
    app.register_blueprint(apitest_routes)
    return app

