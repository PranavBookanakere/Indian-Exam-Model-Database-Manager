import streamlit as st
import pandas as pd
import pymysql

# Connect to the database
conn = pymysql.connect(
    host='localhost',
    user='root',
    passwd='',
    db='indian_exams'
)
cursor = conn.cursor()

# Page title
st.title("Get Students by Exam and Cutoff")

# Create a form for user input
with st.form("get_students_form"):
    exam_name = st.text_input("Enter Exam Name")
    cutoff_marks = st.number_input("Enter Cutoff Marks", min_value=0.0, step=0.1)
    submitted = st.form_submit_button("Get Students")

# Process the submitted data
if submitted:
    # Execute the stored procedure
    cursor.callproc('GetStudentsByExamAndCutoff', (exam_name, cutoff_marks))

    # Fetch the results
    result = cursor.fetchall()

    # Display the results in a DataFrame
    columns = ['Student Name', 'Age']
    df = pd.DataFrame(result, columns=columns)
    
    # Display the DataFrame
    st.dataframe(df)

# Close the database connection
cursor.close()
conn.close()
