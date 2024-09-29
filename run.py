from app import app, db  # Import app and db

# Create the database tables
with app.app_context():
    db.create_all()  # Create all tables if they don't exist

if __name__ == '__main__':
    app.run(debug=True)
