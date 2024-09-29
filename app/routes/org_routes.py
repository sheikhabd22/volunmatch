from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Organization

organization_blueprint = Blueprint('organization', __name__)

@organization_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Register organization logic here
        pass
    return render_template('organization/register.html')

@organization_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Login organization logic here
        pass
    return render_template('organization/login.html')