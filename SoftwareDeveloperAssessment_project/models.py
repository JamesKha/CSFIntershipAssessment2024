from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Response(db.Model):
    """Model for storing user form.

    Attributes:
    - id (int): Unique identifier for each form.
    - name (str): User's name.
    - email (str): User's email address.
    - city (str): User's city.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Response {self.name}>'
