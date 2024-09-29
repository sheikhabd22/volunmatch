from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///volunteer_matching_app.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)  # Initialize SQLAlchemy with the app instance

# Import routes after initializing app and db
from app.routes.volunteer_routes import volunteer_blueprint
app.register_blueprint(volunteer_blueprint)
