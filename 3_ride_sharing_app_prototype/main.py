from flask import Flask, render_template, request, jsonify
import firebase_admin
from firebase_admin import credentials, db

app = Flask(__name__)

# Firebase setup
cred = credentials.Certificate("ride-sharing-app-prototy-4a682-firebase-adminsdk-fbsvc-69dc48d6a6.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://ride-sharing-app-prototy-4a682-default-rtdb.firebaseio.com/'
})

@app.route('/')
def index():
    return render_template('ride_request.html')

@app.route('/request_ride', methods=['POST'])
def request_ride():
    data = request.get_json()
    lat = data.get('lat')
    lng = data.get('lng')

    if lat is None or lng is None:
        return jsonify({'message': 'Missing coordinates'}), 400

    ref = db.reference('ride_requests')
    ref.push({
        'latitude': lat,
        'longitude': lng
    })

    return jsonify({'message': 'Ride requested successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
