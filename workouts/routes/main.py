from flask import Blueprint
from flask import jsonify
main_routes = Blueprint("example", __name__)

all_workouts = [
    {'id': 1, 'name': 'Squat', 'sets': [{'60kg': '2x8'}, {'70kg' : '3x10'}, {'65kg': '1x8'}]},
    {'id': 2, 'name': 'Romanian DL', 'sets' : [{'60kg' : '1x8'}, {'70kg' : '1x9'}, {'60kg' : '1x10'}]}
]

@main_routes.route("/")
def home():
    return jsonify({'workouts' : all_workouts})

@main_routes.route('/about')
def about():
    return "About page"