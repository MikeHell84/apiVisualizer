from flask import Flask, render_template, request, jsonify
import requests
import json
import logging

app = Flask(__name__)

# Configurar logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch_fields', methods=['POST'])
def fetch_fields():
    api_url = request.form['api_url']
    data = fetch_data_from_api(api_url)
    if "error" in data:
        return jsonify({"error": data["error"]})
    else:
        # Obtener los campos disponibles en los datos
        if isinstance(data, list) and len(data) > 0:
            fields = list(data[0].keys())
        else:
            fields = []
        return jsonify({"fields": fields})

def fetch_data_from_api(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        return data[:10]  # Devolver solo las primeras 10 filas
    except requests.RequestException as e:
        logging.error(f"Error al obtener datos: {e}")
        return {"error": "Failed to fetch data from API"}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8050)
