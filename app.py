from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    with open("trade.json", "w") as f:
        json.dump(data, f)
    # Copy file to MT5 JSON path via Dropbox or shared folder if needed
    return jsonify({"status": "success", "received": data}), 200
