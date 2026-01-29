from flask import Flask, jsonify
import requests

app = Flask(__name__)

ORDER_SERVICE_URL = "http://192.168.100.12:8081"

@app.route("/health", methods=["GET"])
def health():
    return jsonify(status="User Service UP")

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify([
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ])

@app.route("/users-with-orders", methods=["GET"])
def users_with_orders():
    orders = requests.get(f"{ORDER_SERVICE_URL}/orders").json()
    return jsonify({
        "users": [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"}
        ],
        "orders": orders
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
