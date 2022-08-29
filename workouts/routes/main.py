from flask import Blueprint, request, render_template
from flask import jsonify, redirect, url_for
from ..database.db import db
from ..models.workout import Workout
from ..models.workout import Set

main_routes = Blueprint("example", __name__)


@main_routes.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        workouts = Workout.query.all()
        return render_template("index.html", workouts=workouts)
    else:

        name = request.form["name"]
        weight = request.form["weight"]
        reps = request.form["reps"]

        new_workout = Workout(name=name)
        new_set = Set(weight=weight, reps=reps, workout=new_workout)

        db.session.add(new_workout)
        db.session.add(new_set)
        db.session.commit()

        
        workouts = Workout.query.all()
        return redirect(url_for('example.home'))
       # return redirect(url_for("/"))
       # return f"{new_workout['name']} has been created", 201

@main_routes.route('/delete/<int:id>', methods=['POST'])
def delete_workout(id):
    workout_to_delete = Workout.query.get(id)
    db.session.delete(workout_to_delete)
    db.session.commit()

    return redirect(url_for('example.home'))


@main_routes.route('/about')
def about():
    return "About page"
    
