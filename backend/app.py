

from flask import Flask, request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os, certifi

load_dotenv()

app = Flask(__name__)

MONGO_URI = os.getenv("MONGO_URI", "")

client = MongoClient(MONGO_URI, tlsCAFile=certifi.where()) if MONGO_URI else None
db = client["assignment3"] if client is not None else None
collection = db["users"] if db is not None else None


@app.route("/submit", methods=["POST"])
def submit():
    try:
        data = request.get_json(force=True)

        # FIXED check
        if collection is None:
            return jsonify({"status": "error", "message": "No MongoDB connection configured."}), 500

        collection.insert_one(data)
        return jsonify({"status": "success"}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/view", methods=["GET"])
def view():
    try:
        # FIXED check
        if collection is None:
            return jsonify({"status": "error", "message": "No MongoDB connection configured."}), 500

        items = list(collection.find({}, {"_id": 0}))
        return jsonify(items), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/api", methods=["GET"])
def api():
    # Task 1 endpoint: read local data.json
    import json, pathlib

    p = pathlib.Path(__file__).parent / "data.json"

    if not p.exists():
        return jsonify({"status": "error", "message": "data.json not found"}), 404

    with open(p, "r", encoding="utf-8") as f:
        data = json.load(f)

    return jsonify(data), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)
