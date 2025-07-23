# RIDE-SHARING-APP-PROTOTYPE-2-ANDROID-TASK-3

*COMPANY:* CODTECH IT SOLUTIONS PVT.LTD

*NAME:* SAMEER KUMAR MISHRA

*INTERN ID:* CT04DZ379

*DOMAIN:* PYTHON PROGRAMMING

*DURATION:* 4 WEEKS

*MENTOR:* NEELA SANTHOSH KUMAR


**Ride Sharing App Prototype**

This is a prototype Ride Sharing App developed using Python (Flask). It includes a backend API, mock driver logic, Firebase support, and a frontend UI using HTML and JavaScript. The app allows users to request rides, store them in a local JSON file or Firebase, and interact with a basic map or UI to simulate the full ride-sharing experience.


**Project Structure**

Here's what each file does:

- app.py – Main Flask app to serve routes and endpoints.

- main.py – Central execution file to launch the app.

- ride_request.py – Handles ride request model and logic.

- driver_logic.py – (Optional) Simulates driver matching/assignment.

- send_ride_request.py – For testing ride requests programmatically.

- ride_request.js – Frontend JavaScript for handling map and request events.

- ride_request.json – Local storage file for ride data (acts like a mock database).

- ride-sharing-app-prototy-*.json – Firebase service account key for integration.


**Features**

- User can request a ride with source and destination.

- Ride data is stored in a JSON file or optionally in Firebase.

- Frontend allows users to interact with map and send data.

- API endpoints return real-time ride data.

- Modular structure separates concerns (routes, drivers, requests).


**Technologies Used**

- Python 3.x

- Flask

- Firebase Admin SDK

- Leaflet.js (map)

- Vanilla JS, HTML


**How to Run the App**

Install dependencies:

- pip install flask firebase-admin

- Ensure the Firebase key file (ride-sharing-app-prototy-*.json) is present.

Run the app using:

- css
- Copy
- Edit
- python main.py

Access in your browser:

- http://127.0.0.1:5000/map → Map interface

- http://127.0.0.1:5000/rides → Ride request form

- http://127.0.0.1:5000/api/rides → View ride data in JSON


**Notes**

- If Firebase is not configured, app defaults to local JSON (ride_request.json).

- send_ride_request.py can be used to send test ride requests without UI.

- driver_logic.py is modular; you can extend it for driver assignment or fare estimation logic.


**Output**

