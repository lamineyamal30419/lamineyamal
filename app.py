from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os
import requests

app = Flask(__name__, static_folder="static", static_url_path="")  # Serve frontend files
CORS(app)  # Enable Cross-Origin Resource Sharing

# Serve the main index.html page
@app.route('/')
def serve_index():
    return send_from_directory("static", "index.html")  # Corrected path

# Serve other static files (CSS, JS, images)
@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory("static", path)

# API endpoint to fetch token price
@app.route('/api/token_info')
def token_info():
    try:
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=lamineyamal&vs_currencies=usd')
        data = response.json()
        price = data.get('lamineyamal', {}).get('usd', "N/A")
    except Exception as e:
        print(f"Error fetching price: {e}")
        price = "Unavailable"
    return jsonify({'price': price})

if __name__ == '__main__':
    app.run(debug=True)


