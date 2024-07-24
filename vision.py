from dotenv import load_dotenv
load_dotenv() #loading all the environment variables
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# function for loading gemini pro model 
model = genai.GenerativeModel('gemini-1.5-flash')
def get_response(input,image):
    if input!='':
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text

# initialize the streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header('Gemini LLM Application')
input = st.text_input('Input Prompt:',key='input') # for textbox

uploaded_file = st.file_uploader('Choose an Image')

image=''
if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file)
        st.image(image,caption='Uploaded Image',use_column_width=True)
    except Exception as e:
        st.error(f"Error opening image: {e}")        
submit = st.button('Tell me about Image')

# function for response

if submit and image:
    response = get_response(input,image)
    st.subheader('The response is')
    st.write(response)