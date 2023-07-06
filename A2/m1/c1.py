# all firestore functions demonstrated here are owned by google. [1]
from flask import Flask, request
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import hashlib

app = Flask(__name__)
CORS(app)
# Allow specific HTTP methods (e.g., GET, POST, PUT) 
CORS(app, methods=['GET', 'POST', 'PUT']) #[2]
# Allow specific headers in the request
CORS(app, headers=['Content-Type']) # [2]
# Allow cookies to be included in cross-origin requests
CORS(app, supports_credentials=True) # [2]

cred = credentials.Certificate('assignment-391215-firebase-adminsdk-5prid-8874894646.json') # [2]
firebase_admin.initialize_app(cred)  # [3]
db = firestore.client()  # [3]

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    #parsing Json
    name = data['name']
    email = data['email']
    password = data['password']
    location = data['location']
    # Hash the password using MD5
    hashed_password = hashlib.md5(password.encode()).hexdigest() #[4]
    # set Values  to firstore collection reg
    reg_ref = db.collection("Reg").document(email)  # [3]
    reg_ref.set({"name": name, "password": hashed_password, "location": location, "email": email})  # [3]
    # print(data)
    return {'status': 'Success'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# References
# [1] 	Google, "The new way to cloud starts here," Google, [Online]. Available: https://cloud.google.com/. [Accessed 07 July 2023].
# [2] 	Python Software Foundation, "Flask-Cors 4.0.0," Python Software Foundation, 2022. [Online]. Available: https://pypi.org/project/Flask-Cors/. [Accessed 04 July 2023].
# [3] 	Google, "Get started with Cloud Firestore," Google, [Online]. Available: https://firebase.google.com/docs/firestore/quickstart. [Accessed 07 July 2023].
# [4] 	Python Software Foundation, "hashlib — Secure hashes and message digests," Python Software Foundation, 03 July 20203. [Online]. Available: https://docs.python.org/3/library/hashlib.html. [Accessed 04 July 2023].


