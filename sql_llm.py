# Prompt --> LLM --> Gemini Pro --> Query --> SQL Database --> Response

from dotenv import load_dotenv
import google.generativeai as genai
import os
import sqlite3
import streamlit as st

load_dotenv()

os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) # configuring API key

def get_response(question,prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0],question])
    return response.text

#function to retrieve query from the sql database
def connect_to_db(sql,db):
    conn = sqlite3.connect(db)
    cur = conn.cursor() # creating cursor
    cur.execute(sql) # for executing query
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    
    # printing rows
    for row in rows:
        print(row)
    return rows
    

## Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - Name, Class, 
    Section, Age, Marks and Grade \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in IT Class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="IT"; 
    also the sql code should not have ``` in beginning or end and sql word in output
    """
]

st.set_page_config(page_title=" Text To SQL LLM App")
st.header(" Text To SQL LLM App using Gemini")
question = st.text_input("Input",key='input')
submit = st.button('Ask the question')
    

# if submit is clicked
if submit:
    response=get_response(question,prompt)
    print(response)
    response=connect_to_db(response,"Student.db")
    st.subheader("Response")
    for row in response:
        print(row)
        st.header(row)