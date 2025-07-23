import pyrebase
import json

firebase_config = json.load(open("firebase_config.json"))
firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()

ride_data = {
    "user": "demo_user",
    "pickup_lat": 28.61,
    "pickup_lng": 77.23,
    "status": "pending"
}

db.child("ride_requests").push(ride_data)
print("Ride requested successfully.")
