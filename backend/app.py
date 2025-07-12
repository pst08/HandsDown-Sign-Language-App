from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows frontend (React) to access backend

@app.route("/api/hello", methods=["GET"])
def hello():
    return jsonify(message="Hello from Flask backend 👋")

if __name__ == "__main__":
    app.run(debug=True)
