from ..database.db import db

class Workout(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    sets = db.relationship('Set', backref='workout', lazy=True)

    def __str__(self):
        return f'<Workout "{self.name}">'

class Set(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.String(80))
    reps = db.Column(db.String(80))
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'),
        nullable=False)
    
    def __str__(self):
        return f'<Set "{self.weight}">'
        
