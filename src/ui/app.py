# Streamlit dashboard
# Developer Comment: Basic UI. Bhargavi to add forms, server calls.
# Layman Comment: Your ship's control panel, Anil.
import streamlit as st
st.title('GitBuddy-AI')
st.write('Enter project:')
project = st.text_area('Project')
if st.button('Start'):
    st.write('AI is setting up...')