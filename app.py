from flask import Flask, request, jsonify
from topsis import topsis

app = Flask(__name__)

@app.route("/")
def home():
    return "TOPSIS web service running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No input data provided"}), 400

    try:
        matrix = data["matrix"]
        weights = data["weights"]
        impacts = data["impacts"]
        labels = data.get("labels")

        scores, ranking = topsis(matrix, weights, impacts, labels)

        return jsonify({
            "scores": scores,
            "ranking": ranking
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run()
