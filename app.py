from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "TOPSIS web service running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if data is None:
        return jsonify({"error": "No input data provided"}), 400

    # Dummy logic (placeholder for TOPSIS)
    response = {
        "input_received": data,
        "score": 0.85,
        "rank": 1
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run()
