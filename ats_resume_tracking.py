from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import pdf2image
import google.generativeai as genai
import base64
import io
import matplotlib.pyplot as plt

load_dotenv()

os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) # configuring API key

def get_response(input,pdf_content,prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        images = pdf2image.convert_from_bytes(uploaded_file.read()) # converting bytes 
        first_page = images[0]
        
        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG') # save it in the form of image
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
# streamlit app
st.set_page_config(page_title="ATS Resume Tracker")
st.header('ATS Resume Tracking App Protocol')
input_text = st.text_area('Job Description:',key='input')
uploaded_file = st.file_uploader('Upload you resume PDF...')

if uploaded_file is not None:
    st.write("PDF uploaded Successfully")

    
s1= st.button('Tell me About the Resume')  
s2= st.button('What are the keywords that are missing')  
s3= st.button('Percentage Match')
s4= st.button('How can I improve my skills')  



input_prompt1 = """
 You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of the field of any one job role like  Data science,full stack web development,
android developement,big data analytics,mlops,devops,data analyst,Computer vision,NLP,Artificial intelligence and your task
is to review the resume against the provided job description. give me the keywords missing in the provided resume from job description.
"""

input_prompt3 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of and field of job role like Data science,full stack web development,
android developement,big data analytics,mlops,devops,data analyst,Computer vision,NLP,Artificial intelligence and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

input_prompt4 = """You are an experienced HR with Tech experience in the feild of any one job role like Data science,full stack web development,
android developement,big data analytics,mlops,devops,data analyst,Computer vision,NLP,Artificial intelligence and your task
is to review the provided resume against the job description for these profiles. Please share your professional evaluation on 
whether the candidate's profile aligns with the role. Highlight the strengths and weaknesses of the applicant in relation to the 
specified job requirements and roles.
"""

if s1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_response(input_prompt1,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

elif s2:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_response(input_prompt2,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

elif s3:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_response(input_prompt3,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)  
        if response.get("match_percentage"):
            match_percentage = float(response["match_percentage"])
            match_data = [match_percentage]       
    else:
        st.write("Please uplaod the resume")
        
elif s4:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_response(input_prompt4,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

