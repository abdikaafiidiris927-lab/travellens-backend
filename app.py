from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"status": "TravelLens backend is running"})

@app.route("/scan", methods=["POST"])
def scan_image():
    return jsonify({
        "location": "Eiffel Tower",
        "country": "France",
        "tips": "Beware of pickpockets around tourist areas."
    })

@app.route("/translate", methods=["POST"])
def translate():
    data = request.json
    text = data.get("text", "")
    target = data.get("target", "en")
    return jsonify({"translated_text": f"[{target}] {text}"})

@app.route("/currency", methods=["GET"])
def currency():
    return jsonify({
        "from": "USD",
        "to": "EUR",
        "rate": 0.92
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
