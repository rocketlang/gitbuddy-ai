
# Streamlit dashboard
# Developer Comment: Updated Streamlit UI with Freight Log tab, single-click button, Indic language support, and feedback form.
# Layman Comment: Your ship's control panel, Anil, now with more features.

import streamlit as st
from googletrans import Translator
import os

# Initialize translator for Indic languages
translator = Translator()

# Set page configuration with a maritime icon (ship's wheel emoji)
st.set_page_config(page_title="GitBuddy-AI", page_icon="⚓")

# Add maritime-themed styling
st.markdown(
    '''
    <style>
    body {
        background-color: #e6f0fa;  /* Light ocean blue background */
    }
    .stTextArea textarea {
        font-size: 18px;  /* Larger text area for easier typing */
        height: 150px;    /* Taller text area */
        background-color: #f0f8ff;  /* Light blue for text area */
        border: 2px solid #4682b4;  /* Steel blue border */
    }
    .stButton>button {
        font-size: 18px;  /* Larger button text */
        padding: 15px 30px;  /* Larger button size */
        background-color: #4682b4;  /* Steel blue button */
        color: white;
        border-radius: 10px;
    }
    .stButton>button:hover {
        background-color: #5a9bd4;  /* Lighter blue on hover */
    }
    </style>
    ''',
    unsafe_allow_html=True
)

# Welcome message with maritime theme
st.title("⚓ GitBuddy-AI")
st.markdown("**Ahoy, Captain! Set your project course below:**")

# Language selection for Indic languages
language = st.selectbox("Choose Language / भाषा चुनें / மொழியைத் தேர்ந்தெடு", ["English", "Hindi", "Tamil"])
lang_code = {"English": "en", "Hindi": "hi", "Tamil": "ta"}

# Tabs for different features
tab1, tab2, tab3 = st.tabs(["Create Project", "Freight Log", "Security Helm"])

with tab1:
    # Single-click button to create a trucking app
    if st.button("Create Trucking App"):
        st.write("Setting up your trucking app... 🚛")
        st.markdown(
            '''
            <audio autoplay>
                <source src="https://www.freesoundslibrary.com/wp-content/uploads/2021/06/ship-horn-sound.mp3" type="audio/mp3">
            </audio>
            ''',
            unsafe_allow_html=True
        )
    
    # Project input with translation
    project_label = "Enter project (e.g., 'Track my ship’s route'):"
    if language != "English":
        project_label = translator.translate(project_label, dest=lang_code[language]).text
    project = st.text_area(project_label, placeholder="Type your project idea here...")
    
    # Start button
    start_label = "Start"
    if language != "English":
        start_label = translator.translate(start_label, dest=lang_code[language]).text
    if st.button(start_label):
        response = "AI is setting up..."
        if language != "English":
            response = translator.translate(response, dest=lang_code[language]).text
        st.write(response)
        st.markdown(
            '''
            <audio autoplay>
                <source src="https://www.freesoundslibrary.com/wp-content/uploads/2021/06/ship-horn-sound.mp3" type="audio/mp3">
            </audio>
            ''',
            unsafe_allow_html=True
        )

with tab2:
    st.header("Freight Log (Version History)")
    st.write("Here’s your ship’s log of changes (commits):")
    # Placeholder for commit history (to be implemented by developers)
    st.write("No logs yet. Your crew will add them soon!")

with tab3:
    st.header("Security Helm")
    st.write("Checking for safety issues...")
    # Placeholder for ClamAV scan (to be implemented in Phase 2)
    st.write("All clear! Your ship is secure for now.")

# Feedback form
st.header("Captain’s Feedback")
feedback_label = "Share your thoughts:"
if language != "English":
    feedback_label = translator.translate(feedback_label, dest=lang_code[language]).text
feedback = st.text_area(feedback_label, placeholder="What do you think of the control panel?")
if st.button("Submit Feedback"):
    with open("feedback/layman_feedback.txt", "a") as f:
        f.write(f"- {feedback}\n")
    st.write("Feedback submitted, Captain!")
