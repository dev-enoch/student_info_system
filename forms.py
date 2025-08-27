from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=150)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class StudentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=150)])
    student_id = StringField('Student ID', validators=[DataRequired(), Length(min=5, max=50)])
    department = StringField('Department', validators=[DataRequired(), Length(min=2, max=100)])
    submit = SubmitField('Submit')