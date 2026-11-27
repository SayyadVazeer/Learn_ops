from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True
)

@app.route("/")
def home():
    visits = redis_client.incr("visit_count")

    return jsonify({
        "message": "Welcome to Python + Redis Docker Project!",
        "total_visits": visits
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
