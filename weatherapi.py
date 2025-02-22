from flask import Flask, render_template, request
import requests # type: ignore

app = Flask(__name__)

API_KEY = 'd3c4a5a4de756a0ec611e22f802db0a5'  # Replace with your API key

@app.route('/')
def home():
    return render_template('weather.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form.get('city')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()
    if data['cod'] == 200:
        weather_data = {
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
        return render_template('weather.html', weather=weather_data)
    else:
        return render_template('weather.html', error="City not found")

if __name__ == '__main__':
    app.run(debug=True)
