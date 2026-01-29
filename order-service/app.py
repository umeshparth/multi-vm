from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify(status="Order Service UP")

@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify([
        {"order_id": 101, "item": "Laptop"},
        {"order_id": 102, "item": "Mobile"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
