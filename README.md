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

## Function to load Gemini Pro Vision
model = genai.GenerativeModel('gemini-pro-vision')

## Extracting Information from Images
def get_gemini_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    return response.text

## Converting Image to Bytes with Information
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

##def input_image_details(uploaded_file):
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



Executing Gemini Pro Vision API Call

python

# If submit button is clicked
if submit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader("The Response is ")
    st.write(response)

# Usage

    Run the Streamlit app using the provided setup instructions.
    Upload an image in JPG, JPEG, or PNG format.
    Enter a prompt in the input field to instruct the system.
    Click the "Tell me about this image" button to receive information extracted from the image.

Prompt Example

python

input_prompt = """
You are an expert in understanding images provided in jpeg and png formats. We will upload an image, and you will have to answer questions about that uploaded image.
"""

Contributions

Contributions are welcome! Feel free to submit issues or pull requests.



