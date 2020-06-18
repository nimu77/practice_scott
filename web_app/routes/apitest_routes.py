from flask import Blueprint, render_template, request

apitest_routes = Blueprint("apitest_routes", __name__)

api_path = 'https://rickandmortyapi.com/graphql/'

@apitest_routes.route("/retrieve")
def api_return():
    return render_template('api_results.html')