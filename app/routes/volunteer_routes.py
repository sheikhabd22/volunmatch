# app/routes/volunteer_blueprint.py
from flask import Blueprint, render_template, request, redirect, url_for
from app.models.volunteer_model import Volunteer
from app import db

volunteer_blueprint = Blueprint('volunteer', __name__)

@volunteer_blueprint.route('/volunteer/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        preferences = request.form['preferences']

        # Create a new volunteer object
        volunteer = Volunteer(name=name, email=email, password=password, preferences=preferences)
        db.session.add(volunteer)
        db.session.commit()

        return redirect(url_for('volunteer.login'))
    return render_template('volunteer/register.html')

@volunteer_blueprint.route('/volunteer/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Find volunteer by email
        volunteer = Volunteer.query.filter_by(email=email).first()

        # Check if volunteer exists and if the password is correct
        if volunteer and volunteer.password == password:
            return redirect(url_for('volunteer.profile'))
    return render_template('volunteer/login.html')

@volunteer_blueprint.route('/volunteer/profile')
def profile():
    return render_template('volunteer/profile.html')
