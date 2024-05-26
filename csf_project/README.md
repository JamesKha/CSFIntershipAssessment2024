
CSF Project - Weather API
This API allows users to submit feedback along with their name, email, and city, and retrieve weather information for the specified city.
(This RESTful API uses the OpenWeather API)

Instructions for running the API:

1. Ensure you have Python installed.
2. Clone this repository to your machine.
3. Install the required dependencies by running: pip install -r requirements.txt.
4. Create a .env file in the project's root directory with the following environment variables:
SQLALCHEMY_DATABASE_URI: The URI for your SQLite database (e.g., sqlite:///data.db).
SECRET_KEY: A secret key for CSRF protection in Flask (e.g., mysecretkey).
OPENWEATHER_API_KEY: Your API key for the OpenWeatherMap API (obtain one at https://home.openweathermap.org/users/sign_up).
5. Run the Flask application by executing: python app.py.
6. Access the API at http://localhost:5000/.

Upon form submission, the user's information will be stored in the SQLite database, but weather data will not be collected at that time.
(Due to potential data discrepancies between the submission and the actual weather conditions, the database may not reflect the weather at the exact time of submission.)

Endpoints:

-POST /: Submit form data.
-GET /responses/<id>: Retrieve form fields by ID.
-GET /responses: Retrieve all form data fields.
-POST /weather: Retrieve weather information for a city.