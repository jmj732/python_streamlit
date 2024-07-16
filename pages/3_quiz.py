import streamlit as st

score = 0

if 'ke' not in st.session_state:
    st.session_state.ke = "풀지 않음"
st.subheader("Quiz-1")
if st.button("바닥은 깨끗이 닦자."):
    if 'ke' in st.session_state:
        st.session_state.ke = "정답"
        score += 33
if st.button("바닥은 깨끗히 닦자."):
    if 'ke' in st.session_state:
        st.session_state.ke = "오답"

if 'k' not in st.session_state:
    st.session_state.k = "풀지 않음"
st.subheader("Quiz-2")
if st.button("오랜지주스 마실래?"):
    if 'k' in st.session_state:
        st.session_state.k = "정답"
        score += 33
if st.button("오랜지쥬스 마실래?"):
    if 'k' in st.session_state:
        st.session_state.k = "오답"

if 'e' not in st.session_state:
    st.session_state.e = "풀지 않음"
st.subheader("Quiz-3")
if st.button("우유곽 재활용하자."):
    if 'e' in st.session_state:
        st.session_state.e = "오답"
if st.button("우유갑 재활용하자."):
    if 'e' in st.session_state:
        st.session_state.e = "정답"
        score += 33
st.subheader("",divider="blue")
if st.button("점수 확인"):
    st.write(score)
    st.write("뭐가 틀린지 궁금하다면 result로 ㄱㄱ")
