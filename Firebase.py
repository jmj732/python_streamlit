import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('secrets.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://python-59598-default-rtdb.firebaseio.com'
})

ref = db.reference()
ref.set({"id": "1413", "name": "조재민"})
