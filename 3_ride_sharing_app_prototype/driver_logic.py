import pyrebase
import json

firebase_config = json.load(open("firebase_config.json"))
firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()

driver_info = {
    "name": "Driver A",
    "location": {"lat": 28.60, "lng": 77.20},
    "vehicle": "Swift",
    "rating": 4.5
}

db.child("drivers").push(driver_info)
print("Driver info uploaded.")
