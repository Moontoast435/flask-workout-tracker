from flask import Blueprint

main_routes = Blueprint("example", __name__)

@main_routes.route("/")
def home():
    return "Hello, this is a basic flask app."