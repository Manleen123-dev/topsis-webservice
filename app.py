from flask import Flask, request, jsonify
from flask_cors import CORS
from topsis import topsis

app = Flask(__name__)
CORS(app)   # ✅ THIS LINE IS IMPORTANT

@app.route("/")
def home():
    return "TOPSIS backend running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    matrix = data["matrix"]
    weights = data["weights"]
    impacts = data["impacts"]
    labels = data["labels"]

    scores, ranking = topsis(matrix, weights, impacts, labels)

    return jsonify({
        "scores": scores,
        "ranking": ranking
    })

if __name__ == "__main__":
    app.run()

