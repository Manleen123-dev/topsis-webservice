from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "TOPSIS web service running"

if __name__ == "__main__":
    app.run()
