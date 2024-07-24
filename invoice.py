from dotenv import load_dotenv
load_dotenv() #loading all the environment variables
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# function for loading gemini pro model 
model = genai.GenerativeModel('gemini-1.5-flash')

def get_respone(input,image,prompt):
    response = model.generate_content([input,image[0],prompt])
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
st.set_page_config(page_title="MultiLanguage Invoice Extractor")
st.header('MultiLanguage Invoice Extractor')
input = st.text_input('Input Prompt:',key='input') # for textbox

uploaded_file = st.file_uploader('Choose an Image')

image=''
if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file)
        st.image(image,caption='Uploaded Image',use_column_width=True)
    except Exception as e:
        st.error(f"Error opening image: {e}")        
submit = st.button('Tell me about Invoice')


input_prompt = """
               You are an expert in understanding invoices.
               You will receive input images as invoices &
               you will have to answer questions based on the input image
               The invoice is might be in all languages of india such as hindi, gujarati, marathi, bengali, malayalam, tamil, telugu and english.
               """
if submit:
    image_data = input_image_details(uploaded_file)
    response = get_respone(input_prompt,image_data,input)
    st.subheader('Response')
    st.write(response)