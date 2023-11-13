from flask import Flask
import requests, os
from waitress import serve

app = Flask(__name__)

def get_weather(api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": "Medellin",
        "appid": api_key,
        "units": "metric",
        "lang": "es"
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

@app.route('/weather', methods=['GET'])
def weather_route():
    try:
        api_key = os.environ['API_KEY']
    except:
        return "No se ha encontrado la API_KEY"
    weather_data = get_weather(api_key)
    return weather_data

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    serve(app, host='0.0.0.0', port=port)
