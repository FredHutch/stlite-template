import streamlit as st

name = st.text_input('Your name')
st.write("Hello,", name or "world", "!")