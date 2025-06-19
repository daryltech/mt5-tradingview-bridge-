from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "MT5 Webhook Server is live!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    with open("trade.json", "w") as f:
        json.dump(data, f)
    print("Webhook Received:", data)
    return jsonify({"status": "success", "received": data}), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Render sets PORT automatically
    app.run(host='0.0.0.0', port=port)
