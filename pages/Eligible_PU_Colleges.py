'''
import streamlit as st
import pymysql
import pandas as pd

# Function to call the MySQL stored procedure for displaying eligible institutions for PU colleges
def call_pu_colleges_procedure(student_id, exam_name, student_marks):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='16020byaadav',
        database='indian_exams',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            # Call your stored procedure for PU colleges here
            cursor.callproc('DisplayEligibleInstitutionsForStudent', (student_id, exam_name, student_marks))
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

# Function to call the MySQL stored procedure for displaying eligible institutions for universities
def call_universities_procedure(student_id, exam_name, student_marks):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='16020byaadav',
        database='indian_exams',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            # Call your stored procedure for universities here
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
        password='16020byaadav',
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
def insert_into_pu_admission(admission_data):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='16020byaadav',
        database='indian_exams',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            # Insert data into PU_admission table
            query = "INSERT INTO PU_admission (student_id, college_id, admission_date) VALUES (%s, %s, CURDATE())"
            cursor.execute(query, (admission_data['student_id'], admission_data['college_id']))
            connection.commit()
    finally:
        connection.close()

# Function to insert data into University_admission table
def insert_into_university_admission(admission_data):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='16020byaadav',
        database='indian_exams',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            # Insert data into University_admission table
            query = "INSERT INTO University_admission (student_id, university_id, admission_date, scholarship) VALUES (%s, %s, CURDATE(), 0)"
            cursor.execute(query, (admission_data['student_id'], admission_data['university_id']))
            connection.commit()
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
stud_id = st.number_input('Enter Student ID:', min_value=0, step=1)
name_exam = st.text_input('Enter Exam Name:')
stud_marks = st.number_input('Enter Student Marks:', min_value=0)

# Button to execute the stored procedure for finding eligible institutions for PU colleges
if st.button('Find Eligible Institutions for PU Colleges'):
    # Display the eligible institutions obtained during the initial call
    eligible_pu_colleges = call_pu_colleges_procedure(stud_id, name_exam, stud_marks)
    st.write('Eligible PU Colleges:')
    for row in eligible_pu_colleges:
        st.write(f"{row['Institute_name']} (College ID: {row['college_id']})")

    # Form to fill PU_admission table
    with st.form("PU Admission Form"):
        student_id_form = st.number_input('Enter Student ID:', min_value=0, step=1)
        college_id_form = st.number_input('Enter College ID for Admission:', min_value=0, step=1)
        submitted_pu = st.form_submit_button('Submit PU College Admission')

        if submitted_pu:
            st.write("Form submitted!")
            st.write(f"College ID: {college_id_form}")
          
            admission_data = {'student_id': student_id_form, 'college_id': college_id_form}
            insert_into_pu_admission(admission_data)
            st.success("PU College Admission record submitted successfully!")

# Button to execute the stored procedure for finding eligible institutions for universities
if st.button('Find Eligible Institutions for Universities'):
    # Display the eligible institutions obtained during the initial call
    eligible_universities = call_universities_procedure(stud_id, name_exam, stud_marks)
    st.write('Eligible Universities:')
    for row in eligible_universities:
        st.write(f"{row['Institute_name']} (University ID: {row['university_id']})")

    # Form to fill University_admission table
    with st.form("University Admission Form"):
        student_id_form = st.number_input('Enter Student ID:', min_value=0, step=1)
        university_id_form = st.number_input('Enter University ID for Admission:', min_value=0, step=1)
        submitted_uni = st.form_submit_button('Submit University Admission')

        if submitted_uni:
            # Insert data into University_admission table
            admission_data = {'student_id': student_id_form, 'university_id': university_id_form}
            insert_into_university_admission(admission_data)
            st.success("University Admission record submitted successfully!")
'''



import streamlit as st
import pymysql
import pandas as pd

# Function to call the MySQL stored procedure for displaying eligible institutions
def call_stored_procedure(student_id, exam_name, student_marks):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='16020byaadav',
        database='indian_exams',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            # Call your stored procedure here
            cursor.callproc('DisplayEligibleInstitutionsForStudent', (student_id, exam_name, student_marks))
            result = cursor.fetchall()
            return result
    finally:
        connection.close()


# Function to display result table
def display_result_table():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='16020byaadav',
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
def insert_into_pu_admission(admission_data):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='16020byaadav',
        database='indian_exams',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            # Insert data into PU_admission table
            query = "INSERT INTO PU_admission (student_id, college_id, admission_date) VALUES (%s, %s, CURDATE())"
            cursor.execute(query, (admission_data['student_id'], admission_data['college_id']))
            connection.commit()
    finally:
        connection.close()

def display_pu_admission_table():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='16020byaadav',
        database='indian_exams',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            # Fetch and display PU_admission table query
            query = "SELECT * FROM PU_admission"
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
        st.write(f"{row['Institute_name']} (ID: {row['college_id']})")


# Button to select from the list of eligible colleges
selected_colleges = st.multiselect('Select Eligible Colleges', [(row['college_id'], row['Institute_name']) for row in eligible_institutions])

# Display the selected colleges
st.write('Selected Colleges:')
for college_id, college_name in selected_colleges:
    st.write(f"{college_name} (ID: {college_id})")

# Form to fill PU_admission table
with st.form("PU Admission Form"):
    student_id_form = st.number_input('Enter Student ID:', min_value=0, step=1)
    college_id_form = st.number_input('Enter College ID:', min_value=0, step=1)
    submitted = st.form_submit_button('Submit Admission')

    if submitted:
        # Insert data into PU_admission table
        admission_data = {'student_id': student_id_form, 'college_id': college_id_form}
        insert_into_pu_admission(admission_data)
        st.success("Admission record submitted successfully!")

if st.button('View PU Admission Table'):
    # Fetch and display PU_admission table
    pu_admission_table = display_pu_admission_table()
    if not pu_admission_table:
        st.warning("No data found in the PU_admission table.")
    else:
        df_pu_admission = pd.DataFrame(pu_admission_table)
        st.write('PU Admission Table:')
        st.dataframe(df_pu_admission)

