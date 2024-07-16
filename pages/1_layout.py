import streamlit as st

st.write(st.session_state.key1)

col1,col2, = st.columns(2)
with col1:
    st.title("quiz1")
    
with col2:
    st.title("quiz2")