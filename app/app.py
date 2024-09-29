from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.routes import volunteer

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///volunteer_matching_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.register_blueprint(volunteer)

if __name__ == '__main__':
    app.run(debug=True)