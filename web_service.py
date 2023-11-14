from flask import Flask, render_template, jsonify
from waitress import serve
import requests, os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def weather_route():
    response = requests.get('http://weather:5000/weather')
    weather_data = response.json()
    return jsonify(weather_data)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 80))
    serve(app, host='0.0.0.0', port=port)
