from flask import Flask, jsonify
import requests

app = Flask(__name__)

PRODUCT_SERVICE_URL = "http://192.168.100.12:8081"

@app.route("/health", methods=["GET"])
def health():
    return jsonify(status="Customer Service UP")

@app.route("/customers", methods=["GET"])
def get_users():
    return jsonify([
        {"id": 1, "name": "Khanak"},
        {"id": 2, "name": "Shagun"}
    ])

@app.route("/customers-with-products", methods=["GET"])
def customers_with_products():
    products = requests.get(f"{PRODUCT_SERVICE_URL}/orders").json()
    return jsonify({
        "users": [
            {"id": 1, "name": "Khanak"},
            {"id": 2, "name": "Shagun"}
        ],
        "products": products
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
