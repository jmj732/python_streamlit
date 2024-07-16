import streamlit as st
import pandas as pd
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('secrets.json')
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://python-59598-default-rtdb.firebaseio.com'
    })

id = st.number_input("학번", value= None)
name = st.text_input("이름")

ref = db.reference("id","name")
if ref.get(id) == id and ref.get(name) == name:
    st.title("success")




