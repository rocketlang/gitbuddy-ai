
# Streamlit dashboard
# Developer Comment: Updated Streamlit UI with maritime theme for layman interaction. Bhargavi to expand with AG-UI integration.
# Layman Comment: Your ship's control panel, Anil, now with a maritime look and feel.

import streamlit as st

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

# Text area for project input
project = st.text_area("Enter project (e.g., 'Track my ship’s route'):", placeholder="Type your project idea here...")

# Start button with ship’s horn sound effect
if st.button("Start"):
    st.write("AI is setting up...")
    # Play a ship’s horn sound using an online audio file
    st.markdown(
        '''
        <audio autoplay>
            <source src="https://www.freesoundslibrary.com/wp-content/uploads/2021/06/ship-horn-sound.mp3" type="audio/mp3">
        </audio>
        ''',
        unsafe_allow_html=True
    )
