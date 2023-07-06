# all firestore functions demonstrated here are owned by google. [1]


from flask import Flask, request
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time,json

app = Flask(__name__)
CORS(app) # [2]
# Allow specific HTTP methods (e.g., GET, POST, PUT)
CORS(app, methods=['GET', 'POST', 'PUT']) # [2]
# Allow specific headers in the request
CORS(app, headers=['Content-Type']) # [2]
# Allow cookies to be included in cross-origin requests
CORS(app, supports_credentials=True) # [2]

cred = credentials.Certificate('assignment-391215-firebase-adminsdk-5prid-8874894646.json') # [3]
firebase_admin.initialize_app(cred) # [3]
db = firestore.client() # [3]

def user_online():
    users = []
    collection_ref = db.collection('state') # [3]
    query = collection_ref.where('online', '==', True).stream() # [3]
    for doc in query:
        users.append(doc.id)
    return users

@app.route('/dashboard', methods=['POST'])
def dashboard():
    users = user_online()
    return {'users': users}

@app.route('/set_state', methods=['POST'])
def set_state():
    data = request.json
    email = data['email']
    timestamp = str(time.time())
    state_ref = db.collection("state").document(email) # [3]
    state_ref.set({"online": False, "offline": True, "timestamp": timestamp}) # [3]
    return {'status': 'Success'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

# References
# [1] 	Google, "The new way to cloud starts here," Google, [Online]. Available: https://cloud.google.com/. [Accessed 07 July 2023].
# [2] 	Python Software Foundation, "Flask-Cors 4.0.0," Python Software Foundation, 2022. [Online]. Available: https://pypi.org/project/Flask-Cors/. [Accessed 04 July 2023].
# [3] 	Google, "Get started with Cloud Firestore," Google, [Online]. Available: https://firebase.google.com/docs/firestore/quickstart. [Accessed 07 July 2023].
