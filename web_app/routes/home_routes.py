from flask import Blueprint, render_template, request

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def our_home():
    return render_template('form.html')