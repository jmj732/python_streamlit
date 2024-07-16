import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
import streamlit as st
key_dict = json.loads(st.secrets["textkey"])
# Fetch the service account key JSON file contents
cred = credentials.Certificate(key_dict)

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://python-59598-default-rtdb.firebaseio.com'
})

ref = db.reference()
ref.set({"id": "1413", "name": "조재민"})
