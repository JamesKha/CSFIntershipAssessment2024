from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Form for capturing user feedback, including name, email, and city
# Validators ensure that required fields are filled out
class FeedbackForm(FlaskForm):
    """Form for capturing user feedback.

    Attributes:
    - name (StringField): Input field for user's name.
    - email (StringField): Input field for user's email address.
    - city (StringField): Input field for user's city.
    - submit (SubmitField): Button for submitting the form.
    """
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    submit = SubmitField('Submit')
