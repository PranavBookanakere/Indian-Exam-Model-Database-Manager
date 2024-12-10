import streamlit as st
import pymysql
import pandas as pd

# Function to call the MySQL stored procedure for displaying eligible institutions
def call_stored_procedure(student_id, exam_name, student_marks):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='indian_exams',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            # Call your stored procedure here
            cursor.callproc('DisplayEligibleInstitutionsForStudent_University', (student_id, exam_name, student_marks))
            result = cursor.fetchall()
            return result
    finally:
        connection.close()


# Function to display result table
def display_result_table():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='indian_exams',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            # Fetch and display result table query
            query = "SELECT * FROM Result"
            cursor.execute(query)
            result_table = cursor.fetchall()
            return result_table
    finally:
        connection.close()

# Function to insert data into PU_admission table
def insert_into_uni_admission(admission_data):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='indian_exams',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            # Insert data into University_admission table
            query = "INSERT INTO University_admission (student_id, university_id, admission_date, scholarship) VALUES (%s, %s, CURDATE(),0)"
            cursor.execute(query, (admission_data['student_id'], admission_data['university_id']))
            connection.commit()
    finally:
        connection.close()

def display_uni_admission_table():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='indian_exams',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            # Fetch and display University_admission table query
            query = "SELECT * FROM University_admission"
            cursor.execute(query)
            pu_admission_table = cursor.fetchall()
            return pu_admission_table
    finally:
        connection.close()


# Button to display result table
if st.button('Display Result Table'):
    # Fetch and display result table
    result_table = display_result_table()
    if not result_table:
        st.warning("No data found in the Result table.")
    else:
        df_result = pd.DataFrame(result_table)
        st.write('Result Table:')
        st.dataframe(df_result)

# Streamlit UI
st.title('Eligible Institutions Finder for Students')

# User input
student_id = st.number_input('Enter Student ID:', min_value=0, step=1)
exam_name = st.text_input('Enter Exam Name:')
student_marks = st.number_input('Enter Student Marks:', min_value=0.0)

# Call the stored procedure once and store the result
eligible_institutions = call_stored_procedure(student_id, exam_name, student_marks)


# Button to execute the stored procedure for finding eligible institutions
if st.button('Find Eligible Institutions'):
    # Display the eligible institutions obtained during the initial call
    st.write('Eligible Colleges:')
    for row in eligible_institutions:
        st.write(f"{row['Institute_name']} (ID: {row['university_id']})")


# Button to select from the list of eligible colleges
selected_colleges = st.multiselect('Select Eligible Colleges', [(row['university_id'], row['Institute_name']) for row in eligible_institutions])

# Display the selected colleges
st.write('Selected Colleges:')
for college_id, college_name in selected_colleges:
    st.write(f"{college_name} (ID: {college_id})")

# Form to fill University_admission table
with st.form("PU Admission Form"):
    student_id_form = st.number_input('Enter Student ID:', min_value=0, step=1)
    university_id_form = st.number_input('Enter University ID:', min_value=0, step=1)
    submitted = st.form_submit_button('Submit Admission')

    if submitted:
        # Insert data into University_admission table
        admission_data = {'student_id': student_id_form, 'university_id': university_id_form}
        insert_into_uni_admission(admission_data)
        st.success("Admission record submitted successfully!")

if st.button('View University Admission Table'):
    # Fetch and display PU_admission table
    uni_admission_table = display_uni_admission_table()
    if not uni_admission_table:
        st.warning("No data found in the University_admission table.")
    else:
        df_uni_admission = pd.DataFrame(uni_admission_table)
        st.write('University Admission Table:')
        st.dataframe(df_uni_admission)

