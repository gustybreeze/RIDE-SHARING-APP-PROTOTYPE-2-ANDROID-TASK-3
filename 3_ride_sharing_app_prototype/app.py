from flask import Flask, request, jsonify
from datetime import datetime
import uuid
import json
import os

app = Flask(__name__)
DATA_FILE = "ride_request.json"


# Load existing rides from file (if file exists)
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        rides_db = json.load(f)
else:
    rides_db = []

# Save ride to JSON file
def save_rides():
    with open(DATA_FILE, "w") as f:
        json.dump(rides_db, f, indent=2)

@app.route('/')
def home():
    return "Ride Sharing App Running!"

@app.route('/request_ride', methods=['POST'])
def request_ride():
    data = request.get_json()
    user_id = data.get("user_id")
    source = data.get("source")
    destination = data.get("destination")

    ride_id = str(uuid.uuid4())
    ride = {
        "ride_id": ride_id,
        "user_id": user_id,
        "source": source,
        "destination": destination,
        "timestamp": datetime.now().isoformat()
    }
    rides_db.append(ride)
    save_rides()  # save to file
    return jsonify({"message": "Ride requested successfully", "ride": ride}), 201

@app.route('/all_rides', methods=['GET'])
def all_rides():
    return jsonify({
        "total_rides": len(rides_db),
        "rides": rides_db
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
