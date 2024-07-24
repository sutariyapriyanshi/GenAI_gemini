from dotenv import load_dotenv
import streamlit as st
import os
import PyPDF2 
import google.generativeai as genai

load_dotenv()

os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) # configuring API key

def get_response(input,pdf_content,prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_text(uploaded_file):
    reader=PyPDF2.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):  # reading pages
        page=reader.pages[page]
        text+=str(page.extract_text()) # extracting text
    return text

# prompt template

input_prompt="""
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in one single string having the structure {{"Job Description Match":"%","MissingKeywords:[]","Profile Summary":""}}"""

st.set_page_config(page_title="ATS Resume Tracker")
st.header('ATS Resume Tracking App Protocol')
jd = st.text_area('Job Description:')
uploaded_file = st.file_uploader('Upload you resume PDF...')
submit = st.button('Submit')

if submit:
    if uploaded_file is not None:
        pdf_content = input_pdf_text(uploaded_file)
        response = get_response(input_prompt, pdf_content, jd)
        st.write(response) 