from workouts import db
from workouts.models.workout import Workout
from workouts.models.workout import Set

# Clear it all out

db.drop_all()

# Set it back up

db.create_all()

# Seed data

w1 = Workout(name="Squat")
w2 = Workout(name="Romanian DL")
s1 = Set(weight="60kg", reps="1x8", workout=w1)
s2 = Set(weight="70kg", reps="1x8", workout=w2)
db.session.add_all([w1, w2])
db.session.add_all([s1, s2])
db.session.commit()