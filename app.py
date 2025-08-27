from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Student
from forms import LoginForm, StudentForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Change this in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Create database and default admin user if not exists
with app.app_context():
    db.create_all()
    if not User.query.filter_by(username='admin').first():
        admin = User(username='admin', password=generate_password_hash('password'))
        db.session.add(admin)
        db.session.commit()

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('index'))
        flash('Invalid username or password')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    search_query = request.form.get('search') if request.method == 'POST' else None
    if search_query:
        students = Student.query.filter(
            (Student.name.like(f'%{search_query}%')) | 
            (Student.student_id.like(f'%{search_query}%'))
        ).all()
    else:
        students = Student.query.all()
    return render_template('index.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
@login_required
def add_student():
    form = StudentForm()
    if form.validate_on_submit():
        if Student.query.filter_by(student_id=form.student_id.data).first():
            flash('Student ID already exists')
            return render_template('add_student.html', form=form)
        student = Student(name=form.name.data, student_id=form.student_id.data, department=form.department.data)
        db.session.add(student)
        db.session.commit()
        flash('Student added successfully')
        return redirect(url_for('index'))
    return render_template('add_student.html', form=form)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update_student(id):
    student = Student.query.get_or_404(id)
    form = StudentForm(obj=student)
    if form.validate_on_submit():
        if Student.query.filter(Student.student_id == form.student_id.data, Student.id != id).first():
            flash('Student ID already exists')
            return render_template('update_student.html', form=form, student=student)
        student.name = form.name.data
        student.student_id = form.student_id.data
        student.department = form.department.data
        db.session.commit()
        flash('Student updated successfully')
        return redirect(url_for('index'))
    return render_template('update_student.html', form=form, student=student)

@app.route('/delete/<int:id>')
@login_required
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    flash('Student deleted successfully')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)