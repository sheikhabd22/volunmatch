from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'  # Replace with your database URI
db = SQLAlchemy(app)

from app.routes.volunteer_routes import volunteer
app.register_blueprint(volunteer)