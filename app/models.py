from app import db, login_manager 
from flask_login import UserMixin

class teacher(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    course_code = db.Column(db.String(10), nullable=False)
    phone = db.Column(db.String(20), nullable=False, unique=True)
    attend = db.Column(db.Boolean, default=False)
    times_present = db.Column(db.Integer, default=0)  

class student(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    index_num = db.Column(db.String(20), nullable=False, unique=True)
    faculty_class = db.Column(db.String(10), nullable=False)
    phone = db.Column(db.String(20), nullable=False, unique=True)
    attend = db.Column(db.Boolean, default=False)
    times_present = db.Column(db.Integer, default=0)  

@login_manager.user_loader
def load_user(user_id):
    return student.query.get(int(user_id)), teacher.query.get(int(user_id))
