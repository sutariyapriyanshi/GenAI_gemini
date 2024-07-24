from dotenv import load_dotenv
load_dotenv() #loading all the environment variables
import streamlit as st
import os
import google.generativeai as genai
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# function for loading gemini pro model 
model = genai.GenerativeModel('gemini-pro')
def get_response(question):
    response = model.generate_content(question)
    return response.text

# initialize the streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header('Gemini LLM Application')
input = st.text_input('Input',key='input') # for textbox
submit = st.button('Ask me Question')

# function for response

if submit:
    response = get_response(input)
    st.write(response)