import streamlit as st

if 'key1' not in st.session_state:
    st.session_state.key1 = "NULL"

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.session_state.key1 = "Hi"
else:
    st.session_state.key1 = "Bye"