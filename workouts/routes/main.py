from flask import Blueprint, request, render_template
from flask import jsonify
from ..database.db import db
from ..models.workout import Workout
from ..models.workout import Set

main_routes = Blueprint("example", __name__)

 # all_workouts = [
    # {'id': 1, 'name': 'Squat', 'sets': [{'60kg': '2x8'}, {'70kg' : '3x10'}, {'65kg': '1x8'}]},
    # {'id': 2, 'name': 'Romanian DL', 'sets' : [{'60kg' : '1x8'}, {'70kg' : '1x9'}, {'60kg' : '1x10'}]}
#]

@main_routes.route("/", methods=["GET"])
def home():
    workouts = Workout.query.all()
    sets = Set.query.all()
    return render_template("index.html", workouts=workouts, sets=sets)

@main_routes.route('/about')
def about():
    return "About page"