# all firestore functions demonstrated here are owned by google. [1]

from flask import Flask, request
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import hashlib
import time
import json


app = Flask(__name__)
CORS(app) #[2]
# Allow specific HTTP methods (e.g., GET, POST, PUT)
CORS(app, methods=['GET', 'POST', 'PUT']) #[2]

# Allow specific headers in the request
CORS(app, headers=['Content-Type']) #[2]

# Allow cookies to be included in cross-origin requests
CORS(app, supports_credentials=True) #[2]

cred = credentials.Certificate('assignment-391215-firebase-adminsdk-5prid-8874894646.json') # [3]
firebase_admin.initialize_app(cred) # [3]
db = firestore.client() # [3]

def user_online():
    users = []
    collection_ref = db.collection('state')
    query = collection_ref.where('online', '==', True).stream()
    for doc in query:
        users.append(doc.id)
    return users

@app.route('/signin', methods=['POST'])
def signin():
    data = request.json
    email = data['email']
    password = data['password']

    # Hash the password using MD5
    hashed_password = hashlib.md5(password.encode()).hexdigest() # [4] 

    reg_ref = db.collection("Reg").document(email)
    doc = reg_ref.get()

    if doc.exists:
        user_data = doc.to_dict()
        if user_data['password'] == hashed_password:
            name = user_data['name']
            location = user_data['location']
            timestamp = str(time.time())
            users = json.dumps(user_online())
            state_ref = db.collection("state").document(email )# [3] 
            state_ref.set({"online": True, "offline": False, "timestamp": timestamp}) # [3] 
            return {'name': name, 'location': location, 'email': email, 'timestamp': timestamp, 'users': users, 'status': 'Success'}
        else:
            return {'status': 'Failure'}
    else:
        return {'status': 'Failure'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

# References
# [1] 	Google, "The new way to cloud starts here," Google, [Online]. Available: https://cloud.google.com/. [Accessed 07 July 2023].
# [2] 	Python Software Foundation, "Flask-Cors 4.0.0," Python Software Foundation, 2022. [Online]. Available: https://pypi.org/project/Flask-Cors/. [Accessed 04 July 2023].
# [3] 	Google, "Get started with Cloud Firestore," Google, [Online]. Available: https://firebase.google.com/docs/firestore/quickstart. [Accessed 07 July 2023].
# [4] 	Python Software Foundation, "hashlib — Secure hashes and message digests," Python Software Foundation, 03 July 20203. [Online]. Available: https://docs.python.org/3/library/hashlib.html. [Accessed 04 July 2023].


docker push northamerica-northeast1-docker.pkg.dev/assignment-391215/c1/c1
docker push northamerica-northeast1-docker.pkg.dev/assignment-391215/c2/c2
docker push northamerica-northeast1-docker.pkg.dev/assignment-391215/c3/c3
docker push northamerica-northeast1-docker.pkg.dev/assignment-391215/frontend/frontend
