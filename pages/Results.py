import streamlit as st
import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='indian_exams'
)

col1, col2 = st.columns(2)


def display_student_details():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM student;')
    info = cursor.fetchall()
    data = [list(ele) for ele in info]

    placeholder = st.empty()
    with placeholder.container():
        columns = ['id', 'name', 'mail', 'phone_no', 'DOB', 'school', 'gender', 'address']
        df = pd.DataFrame(data, columns=columns)
        st.dataframe(df)

    cursor.close()
    conn.commit()

    clear = st.button("Clear", type="primary")
    if clear:
        placeholder.empty()

def display_exam_details():
    cursor = conn.cursor()
    columns = ['exam_id', 'Institution_name','exam_name', 'min_age', 'cut_off_marks','exam_date', 'exam_duration', 'exam_type', 'max_attempts', 'college_id','university_id']
    cursor.execute('SELECT * FROM exam;')
    info = cursor.fetchall()
    data = [list(ele) for ele in info]

    placeholder = st.empty()
    with placeholder.container():
        df = pd.DataFrame(data, columns=columns)
        st.dataframe(df)

    cursor.close()
    conn.commit()

    clear = st.button("Clear", type="primary")
    if clear:
        placeholder.empty()

# Page title
st.title("Upload Result Form 📊")

# Create a form for user input
with st.form("result_upload_form"):
    student_id = st.text_input("Student ID")
    exam_id = st.text_input("Exam ID")
    exam_name = st.text_input("Exam Name")
    date_of_result = st.date_input("Date of Result")
    result_status = st.selectbox("Result Status", ["Pass", "Fail"])
    percentage_marks = st.number_input("Percentage Marks", min_value=0.0)
    submitted = st.form_submit_button("Upload Result")

# Process the submitted data
if submitted:
    result_status = result_status.upper()

    # Insert the data into the 'Result2' table
    cursor = conn.cursor()
    insert_query = "INSERT INTO Result (student_id, exam_id, exam_name, date_of_result, status, percent_marks) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (student_id, exam_id, exam_name, date_of_result, result_status, percentage_marks)
    cursor.execute(insert_query, values)
    conn.commit()
    cursor.close()

    st.write("Uploaded Result:")
    st.write(f"Student ID: {student_id}")
    st.write(f"Exam ID: {exam_id}")
    st.write(f"Exam Name: {exam_name}")
    st.write(f"Date of Result: {date_of_result}")
    st.write(f"Result Status: {result_status}")
    st.write(f"Percentage Marks: {percentage_marks}%")

# Display student details or exam details
if st.button('STUDENT DETAILS'):
    display_student_details()

if st.button('EXAMS'):
    display_exam_details()
