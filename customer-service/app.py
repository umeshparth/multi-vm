from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify(status="Customer Service UP")

@app.route("/customers", methods=["GET"])
def get_customers():
    return jsonify([
        {"id": 1, "name": "Khanak"},
        {"id": 2, "name": "Shagun"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
