from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

db = SQLAlchemy(app)

# Define a SQLAlchemy model for the responses table
class Response(db.Model):
    """Model for storing user responses."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)

# Define a WTForms form for capturing user data
class DataForm(FlaskForm):
    """Form for capturing user info."""
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    city = StringField('City', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Route for submitting and displaying the data form
@app.route('/', methods=['GET', 'POST'])
def index():
    form = DataForm()
    if form.validate_on_submit():
        new_response = Response(name=form.name.data, email=form.email.data, city=form.city.data)
        db.session.add(new_response)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('index.html', form=form)

# Route for retrieving a response by ID
@app.route('/responses/<int:id>', methods=['GET'])
def get_response(id):
    response = Response.query.get(id)
    if not response:
        return jsonify({'message': 'Response not found'}), 404
    return jsonify({
        'id': response.id,
        'name': response.name,
        'email': response.email,
        'city': response.city
    })

# Route for retrieving all responses
@app.route('/responses', methods=['GET'])
def get_all_responses():
    responses = Response.query.all()
    response_list = []
    for response in responses:
        response_list.append({
            'id': response.id,
            'name': response.name,
            'email': response.email,
            'city': response.city
        })
    return jsonify(response_list)

# Route for retrieving weather information for a city
@app.route('/weather', methods=['POST'])
def weather():
    form = DataForm()
    if form.validate_on_submit():
        city = form.city.data
        api_key = os.getenv('OPENWEATHER_API_KEY')
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        weather_data = requests.get(url).json()
        new_response = Response(name=form.name.data, email=form.email.data, city=city)
        db.session.add(new_response)
        db.session.commit()

        return jsonify({
            'message': 'Form submitted successfully',
            'name': form.name.data,
            'email': form.email.data,
            'city': city,
            'weather': weather_data
        })
    return render_template('index.html', form=form)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
