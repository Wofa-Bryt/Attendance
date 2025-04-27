from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,SelectField
from wtforms.validators import DataRequired, Length, EqualTo


class Choice(FlaskForm):
    choice = SelectField('Role', choices=[])


class Teacher(FlaskForm):
    name = StringField('Full name', validators=[DataRequired()])
    phone = StringField('Phone Number' , validators=[DataRequired(), Length(min=10, max=15) ])
    course_code = StringField('Course Code', validators=[DataRequired()])
    submit = SubmitField("Submit") 


class Student(FlaskForm):
    name = StringField('Full name', validators=[DataRequired()])
    phone = StringField('Phone Number' , validators=[DataRequired(), Length(min=10, max=15) ])
    index_num = StringField('Index Number', validators=[DataRequired(), Length(min=10, max=15)])
    faculty_class = StringField('Class', validators=[DataRequired()])
    submit = SubmitField("Submit") 


class Principal(FlaskForm):
    name = StringField('Full name', validators=[DataRequired()])
    password = PasswordField("New Password", validators=[  
        DataRequired(),  
        Length(min=6),  
        EqualTo("confirm", message="Passwords must match")  
    ])  
    confirm = PasswordField("Repeat Password", validators=[DataRequired()])  
    submit = SubmitField("Submit") 