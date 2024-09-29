from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Set your secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///volunteer_matching_app.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Import routes after initializing app and db
from app.routes.volunteer_routes import volunteer_blueprint
app.register_blueprint(volunteer_blueprint)
