from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify(status="Order Service UP")

@app.route("/products", methods=["GET"])
def get_orders():
    return jsonify([
        {"product_id": 101, "item": "Diamond Necklace"},
        {"product_id": 102, "item": "Gold Ring"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
