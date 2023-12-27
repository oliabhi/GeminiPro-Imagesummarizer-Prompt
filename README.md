# Gemini Pro Vision - Multi-Language Image Information Extractor

Gemini Pro Vision is a Streamlit web application that utilizes Google's Generative AI for extracting information from images in multiple languages. This application integrates with the Gemini Pro Vision API and provides an interactive interface to analyze images based on user prompts.

## Functionality

### Loading Gemini Pro Vision Model

```python
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

import streamlit as st 
import os 
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro Vision

model = genai.GenerativeModel('gemini-pro-vision')

# Extracting Information from Images

def get_gemini_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    return response.text

# Converting Image to Bytes with Information
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

# If submit button is clicked
if submit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader("The Response is ")
    st.write(response)


## Usage

1. Run the Streamlit app using the provided setup instructions.
2. Upload an image in JPG, JPEG, or PNG format.
3. Enter a prompt in the input field to instruct the system.
4. Click the "Tell me about this image" button to receive information extracted from the image.

## Input Prompt

You are an expert in understanding images provided in JPEG and PNG formats. We will upload an image, and you will have to answer questions about that uploaded image.


<img src="https://img.shields.io/badge/GIT-black?style=for-the-badge&logo=GIT&logoColor=F05032"/>
<img src="https://img.shields.io/badge/PYTHON-black?style=for-the-badge&logo=python&logoColor=gold"/>
<img src="https://img.shields.io/badge/GIT-black?style=for-the-badge&logo=GIT&logoColor=F05032"/>
<img src="https://img.shields.io/badge/PYTHON-black?style=for-the-badge&logo=python&logoColor=gold"/>
