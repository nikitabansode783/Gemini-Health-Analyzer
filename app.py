from dotenv import load_dotenv
import os
import streamlit as st
from PIL import Image
import random

# Load environment variables from .env file
load_dotenv()

# Mock function to identify food and calculate calories
def identify_food_and_calories(image):
    # This function is a placeholder. Replace with actual model/API call.
    foods = ["Apple", "Banana", "Pizza", "Salad", "Burger"]
    calories = {
        "Apple": 95,
        "Banana": 105,
        "Pizza": 285,
        "Salad": 150,
        "Burger": 354
    }
    identified_food = random.choice(foods)
    return identified_food, calories[identified_food]

def get_calorie_analysis(uploaded_file):
    try:
        image = Image.open(uploaded_file)
        identified_food, calorie_count = identify_food_and_calories(image)
        return identified_food, calorie_count
    except Exception as e:
        return None, f"Error: {str(e)}"

# Set page configuration
favicon_path = 'star.ico'  # Replace with your actual path or URL
st.set_page_config(page_title="Calorie Tracker", page_icon=favicon_path, layout="wide")

# Define colors
PRIMARY_COLOR = "#28a745"
SECONDARY_COLOR = "#6c757d"
BACKGROUND_COLOR = "#f8f9fa"
TEXT_COLOR = "#212529"

# Apply custom CSS
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {BACKGROUND_COLOR};
        color: {TEXT_COLOR};
    }}
    .stButton>button {{
        background-color: {PRIMARY_COLOR};
        color: white;
    }}
    .stTextInput>div>div>input {{
        background-color: white;
        color: black;
    }}
    .stFileUploader>div>div>button {{
        background-color: {PRIMARY_COLOR};
        color: white;
    }}
    .stSpinner>div>div>div {{
        color: {PRIMARY_COLOR};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar for additional information
st.sidebar.title("Instructions")
st.sidebar.info(
    """
    1. Upload a food image (jpg, jpeg, png).
    2. Click the 'Analyze Image' button.
    3. View the identified food and its calorie count.
    """
)

# App title and description
st.title("Calorie Tracker")
st.markdown("### Upload a food image and get detailed calorie analysis")

# Main interface with tabs
tab1, tab2 = st.tabs(["Upload & Analyze", "Analysis Result"])

with tab1:
    st.subheader("Step 1: Upload Your Food Image")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

    submit = st.button("Analyze Image")

with tab2:
    st.subheader("Step 2: View Analysis Result")
    if submit:
        if uploaded_file is not None:
            with st.spinner("Analyzing the food image..."):
                identified_food, calorie_count = get_calorie_analysis(uploaded_file)
                if calorie_count is not None:
                    st.success(f"Identified Food: {identified_food}")
                    st.info(f"Calorie Count: {calorie_count} kcal")
                else:
                    st.error(f"Error: {calorie_count}")
        else:
            st.error("Please upload an image to analyze.")

# Footer with contact information
st.markdown(
    """
    <div style='text-align: center; color: #888;'>
    <p>Developed by Your Name | <a href='mailto:your.email@example.com'>Contact Us</a></p>
    </div>
    """,
    unsafe_allow_html=True
)
