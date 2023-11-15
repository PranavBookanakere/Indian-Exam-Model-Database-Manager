import pymysql
import datetime
import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='16020byaadav',
    database='indian_exams'
)


#cursor = db.cursor()
#cursor.execute(' use indian_exams;')

def insert_student(student_id, student_name, date_of_birth, gender, phone_number, email, address, school):
    cursor = conn.cursor()
    insert_query = "INSERT INTO student (student_id, student_name, date_of_birth, gender, phone_number, mail_id, address, school) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
        
    # Values to be inserted from the user input
    values = (student_id, student_name, date_of_birth, gender, phone_number, email, address, school)
    
    # Execute the INSERT query
    cursor.execute(insert_query, values)
    conn.commit()

    st.write("Student information has been successfully inserted into the database.")

    #creating a dataframe to display the data in a table
    columns = ['id','name','mail','phone_no','DOB','school','gender','address']
    cursor.execute('SELECT * FROM student ; ')
    info = cursor.fetchall()
    data = []
    for ele in info:
        data.append(list(ele))
    #converting the list to a dataframe

    placeholder = st.empty()
    with placeholder.container():
    
        df = pd.DataFrame(data , columns=columns)
        st.dataframe(df)
        cursor.close()

    #creating a button to clear the dataframe 
        clear = st.button("Clear", type="primary")
        if clear:
            placeholder.empty()

    cursor.close()


import streamlit as st
# Page title
st.title("Student Information Form 📝")

# Apply custom CSS for a dark background
st.markdown(
    """
    <style>
        body {
            background-color: #333;  /* Dark background color */
            color: #fff;  /* Text color */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Create a form for user input
with st.form(key='student_form'):
    col1, col2 = st.columns(2)

    # Input fields
    with col1:
        student_id = st.number_input("Student ID",min_value=0)
        #prime_id = int(student_id)
        student_name = st.text_input("Student Name")
        date_of_birth = st.date_input("Date of Birth",min_value=datetime.date(year=1995, month=12, day=31))
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        phone_number = st.text_input("Phone Number")
    with col2:
        email = st.text_input("Email Address")
        address = st.text_area("Address")
        school = st.text_input("School")
    
    # Submission button
    submit_button = st.form_submit_button("Submit")

# Display user input upon submission
if submit_button:
    st.write("Submitted Student Information:")
    st.write(f"Student ID: {student_id}")
    st.write(f"Student Name: {student_name}")
    st.write(f"Date of Birth: {date_of_birth}")
    st.write(f"Gender: {gender}")
    st.write(f"Phone Number: {phone_number}")
    st.write(f"Email Address: {email}")
    st.write(f"Address: {address}")
    st.write(f"School: {school}")

    insert_student(student_id, student_name, date_of_birth, gender, phone_number, email, address, school)

