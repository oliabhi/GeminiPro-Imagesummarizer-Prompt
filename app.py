from dotenv import load_dotenv

load_dotenv() # load all the env variable from .env file

import streamlit as st 
import os 
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini Pro vision

model=genai.GenerativeModel('gemini-pro-vision')

def get_gemini_respone(input,image,prompt):
    response=model.generate_content([input,image[0],prompt])
    return response.text


# convert image to bytes with all info
def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        image_parts=[
            {
                "mime_type": uploaded_file.type,
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file found")



#INIT STREAMLITT APP

st.set_page_config(page_title="Gemini Pro based MultiLanguage IMAGE Information Extractor")
st.write("Welcome to my Gemini Pro app. This is an app which takes image inputs and takes prompt as to what you want to know about the IMAGE.")

st.header("Multi-Lingual Image Extractor")

input=st.text_input("Input_Prompt: " , key="input")
uploaded_file = st.file_uploader("Choose an Image to upload - ", type =["jpg", "jpeg", "png"])
image=""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image:", use_column_width=True)

submit=st.button("Tell me about this image")

input_prompt="""
You are an expert in understanding images provided in jpeg and png formats. We will upload a image and you will have to answer questions about that uploaded image.
"""

# If submit button is clicked
if submit:

    image_data = input_image_details(uploaded_file)
    response=get_gemini_respone(input_prompt,image_data,input)
    st.subheader("The Response is ")
    st.write(response)


    # stuff you can ask to the prompt
    # 