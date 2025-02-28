Weather App

This is a simple Weather App built using Flask and the OpenWeatherMap API. Users can enter a city name to retrieve the current weather conditions.

Features

Search for weather information by city name

Displays temperature in Celsius

Provides a brief weather description

Requirements

To run this project, ensure you have the following installed:

Python 3

Flask

Requests library

Installation

Clone the repository:

git clone https://github.com/yourusername/weather-app.git
cd weather-app

Install dependencies:

pip install flask requests

Get an API key from OpenWeatherMap

Replace API_KEY in weatherapi.py with your API key

Usage

Run the application:

python weatherapi.py

Open your browser and go to:

http://127.0.0.1:5000/

Enter a city name and click "Get Weather"

File Structure

weatherapi.py: Main Flask application handling routes and API requests

templates/weather.html: Frontend HTML template for user interaction

README.md: Documentation for the project

License

This project is licensed under the MIT License.

