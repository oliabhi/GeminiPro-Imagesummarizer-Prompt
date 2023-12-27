# Import statements
from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro Vision
def load_gemini_pro_vision_model():
    return genai.GenerativeModel('gemini-pro-vision')

# Function to get Gemini response
def get_gemini_response(model, input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    return response.text

# Function to convert image to bytes with all information
def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file found")

# Initialize Streamlit app
st.set_page_config(page_title="Image Information Extractor")
st.header("Multi-Lingual Image Extractor")
st.write("Welcome to my app. This is an app that takes image inputs and prompts to extract information about the IMAGE.")

# User inputs
input = st.text_input("input: ", key="input")
uploaded_file = st.file_uploader("Choose an Image to upload - ", type=["jpg", "jpeg", "png"])

# Display uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image:", use_column_width=True)

# Execute Gemini Pro Vision API Call
submit = st.button("Tell me about this image")
input_prompt="""
You are an expert in understanding images provided in jpeg and png formats. We will upload a image and you will have to answer questions about that uploaded image.
"""
# If submit button is clicked
if submit:
    model = load_gemini_pro_vision_model()
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(model, input_prompt, image_data, input)
    st.subheader("The Response is ")
    st.write(response)