from dotenv import load_dotenv
import streamlit as st
import os
import PyPDF2 
import google.generativeai as genai
from PIL import Image
load_dotenv()

os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) # configuring API key

def get_response(input_prompt,image):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input_prompt,image[0]])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        # get the mimetype of uploaded image
        # standardized labels used to identify the nature and format of a file's content.
        return image_parts
    else:
        raise FileNotFoundError('No file uploaded')
    
# initialize the streamlit app
st.set_page_config(page_title="Calorie Adviser LLM App")
st.header('Calorie Adviser LLM App')

uploaded_file = st.file_uploader('Choose an Image')

image=''
if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file)
        st.image(image,caption='Uploaded Image',use_column_width=True)
    except Exception as e:
        st.error(f"Error opening image: {e}")        
submit = st.button('Tell me about total calories')

input_prompt="""
You are an expert in nutritionist where you need to see the food items from the image
               and calculate the total calories, also provide the details of every food items with calories intake
               is below format analyze all the food items 

               1. Item 1 - no of calories
               2. Item 2 - no of calories
               ----
               ----
"""

if submit:
    image_data=input_image_details(uploaded_file)
    response=get_response(input_prompt,image_data)
    st.subheader("The Response is")
    st.write(response)