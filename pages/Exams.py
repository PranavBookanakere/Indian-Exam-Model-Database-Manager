'''import mysql.connector
import pandas as pd
import streamlit as st

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='indian_exams'
)

def insert_exam(institute_name, exam_name, min_age, cut_off_marks, exam_date, duration, exam_type , max_attempts):
    cursor = conn.cursor()
    insert_query = "INSERT INTO Exam ( Institute_name, exam_name, min_age, cut_off_marks, exam_date, exam_duration, exam_type, max_attempts) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s);"
    values = (institute_name, exam_name, min_age, cut_off_marks, exam_date, duration, exam_type, max_attempts)
    cursor.execute(insert_query, values)
    conn.commit()
    

    st.write("The exam has been created and has been added into the database.")

    #creating a dataframe to display the data in a table
    columns = ['exam_id', 'Institute_name', 'exam_name', 'min_age', 'cut_off_marks', 'exam_date', 'exam_duration', 'exam_type', 'max_attempts']
    cursor.execute('SELECT * FROM exam;')
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


st.title('CREATE EXAMS 📚')

# Style the page with a light background and padding
st.markdown(
    """
    <style>
        body {
            background-color: #f4f4f4;
            color: #333;
            padding: 20px;
            font-family: 'Arial', sans-serif;
        }
        .info-container {
            background-color: #FFF;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 5px 5px 15px 5px #ccc;
            margin: 20px 0;
        }
        h2 {
            background-color: #007ACC;
            color: #FFF;
            padding: 10px;
            border-radius: 10px;
        }
        ul {
            list-style: none;
            padding-left: 0;
        }
        li::before {
            margin-right: 5px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Description of the "exam" entity
# ... (remains the same)

# creating form to take input
create = st.button("CREATE", type="primary")
info = False
container = st.empty()

# Create a form for user input
with st.form("exam_form"):

    col1, col2 = st.columns(2)
    
    with col1:
        # Exam ID
        #exam_id = st.number_input("Exam ID", min_value=1)

        # Institute Name
        institute_name = st.text_input("Institute Name")

        # Minimum Age
        min_age = st.number_input("Minimum Age", min_value=0)

        # Cut-off Marks
        cut_off_marks = st.number_input("Cut-off Marks", min_value=0)

        #exam name
        exam_name = st.text_input("Exam Name")

        # Submit button (in the left column)
        submitted = st.form_submit_button("Submit")

    with col2:
        # Date of Examination
        exam_date = st.date_input("Date of Examination")

        # Duration
        duration = st.number_input("Duration (in minutes)", min_value=0)

        # Exam Type
        exam_type = st.selectbox("Exam Type", ["Objective", "Subjective", "Combined"])

        # Maximum Attempts
        max_attempts = st.number_input("Maximum Attempts", min_value=0)

# Process the submitted data
if submitted:
    st.write("Submitted Data:")
    #st.write(f"Exam ID: {exam_id}")
    st.write(f"Institute Name: {institute_name}")
    st.write(f"Minimum Age: {min_age}")
    st.write(f"Cut-off Marks: {cut_off_marks}")
    st.write(f"Date of Examination: {exam_date}")
    st.write(f"Duration: {duration} minutes")
    st.write(f"Exam Type: {exam_type}")
    st.write(f"Maximum Attempts: {max_attempts}")

    insert_exam(institute_name, exam_name, min_age, cut_off_marks, exam_date, duration, exam_type, max_attempts)
'''


import mysql.connector
import pandas as pd
import streamlit as st

# Function to establish a connection to the database
def connect_to_database():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='indian_exams'
    )

# Function to get college IDs from the database
def get_college_ids():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('SELECT college_id FROM PU_college;')
    college_ids = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return college_ids

# Function to display colleges from the database
def display_colleges():
    conn = connect_to_database()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM PU_college;')
    colleges = cursor.fetchall()
    cursor.close()
    conn.close()
    return colleges

# Function to display universities from the database
def display_universities():
    conn = connect_to_database()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM University;')
    universities = cursor.fetchall()
    cursor.close()
    conn.close()
    return universities

# Function to insert exam into the database
def insert_exam(institute_name, exam_name, min_age, cut_off_marks, exam_date, duration, exam_type, max_attempts, college_id, university_id):
    conn = connect_to_database()
    cursor = conn.cursor()
    insert_query = "INSERT INTO Exam (Institute_name, exam_name, min_age, cut_off_marks, exam_date, exam_duration, exam_type, max_attempts, college_id, university_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    values = (institute_name, exam_name, min_age, cut_off_marks, exam_date, duration, exam_type, max_attempts, college_id, university_id)
    cursor.execute(insert_query, values)
    conn.commit()
    cursor.close()
    conn.close()

    st.write("The exam has been created and has been added into the database.")

    # Creating a dataframe to display the data in a table
    columns = ['exam_id', 'Institute_name', 'exam_name', 'min_age', 'cut_off_marks', 'exam_date', 'exam_duration', 'exam_type', 'max_attempts', 'college_id', 'university_id']
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM exam;')
    info = cursor.fetchall()
    data = []
    for ele in info:
        data.append(list(ele))
    # Converting the list to a dataframe
    placeholder = st.empty()
    with placeholder.container():
        df = pd.DataFrame(data, columns=columns)
        st.dataframe(df)
        cursor.close()
        conn.close()

    # Creating a button to clear the dataframe
    clear = st.button("Clear", type="primary")
    if clear:
        placeholder.empty()

# Main Streamlit UI
st.title('CREATE EXAMS 📚')

# Style the page with a light background and padding
st.markdown(
    """
    <style>
        body {
            background-color: #f4f4f4;
            color: #333;
            padding: 20px;
            font-family: 'Arial', sans-serif;
        }
        .info-container {
            background-color: #FFF;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 5px 5px 15px 5px #ccc;
            margin: 20px 0;
        }
        h2 {
            background-color: #007ACC;
            color: #FFF;
            padding: 10px;
            border-radius: 10px;
        }
        ul {
            list-style: none;
            padding-left: 0;
        }
        li::before {
            margin-right: 5px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Creating form to take input
create = st.button("CREATE", type="primary")
display_colleges_button = st.button("Display Colleges", type="secondary")
display_universities_button = st.button("Display Universities", type="secondary")

info = False
container = st.empty()


# Create a form for user input
with st.form("exam_form"):

    col1, col2 = st.columns(2)
    
    with col1:
        # Institute Name
        institute_name = st.text_input("Institute Name")

        # Minimum Age
        min_age = st.number_input("Minimum Age", min_value=0)

        # Cut-off Marks
        cut_off_marks = st.number_input("Cut-off Marks", min_value=0)

        # Exam Name
        exam_name = st.text_input("Exam Name")

        institution_type = st.radio("Select Institution Type", ["College", "University"])

        # College ID
        college_id = st.number_input("Enter College ID", min_value=0) if institution_type == "College" else None

        # University ID
        university_id = st.number_input("Enter University ID", min_value=0) if institution_type == "University" else None

        submitted = st.form_submit_button("Submit")

    with col2:
        # Date of Examination
        exam_date = st.date_input("Date of Examination")

        # Duration
        duration = st.number_input("Duration (in minutes)", min_value=0)

        # Exam Type
        exam_type = st.selectbox("Exam Type", ["Objective", "Subjective", "Combined"])

        # Maximum Attempts
        max_attempts = st.number_input("Maximum Attempts", min_value=0)

# Process the submitted data
if submitted:
    st.write("Submitted Data:")
    st.write(f"Institute Name: {institute_name}")
    st.write(f"Minimum Age: {min_age}")
    st.write(f"Cut-off Marks: {cut_off_marks}")
    st.write(f"Date of Examination: {exam_date}")
    st.write(f"Duration: {duration} minutes")
    st.write(f"Exam Type: {exam_type}")
    st.write(f"Maximum Attempts: {max_attempts}")

    if college_id == None:
        st.write(f"University ID: {university_id}")

    else:
        st.write(f"College ID: {college_id}")    
    

    insert_exam(institute_name, exam_name, min_age, cut_off_marks, exam_date, duration, exam_type, max_attempts, college_id, university_id)

elif display_colleges_button:
    colleges = display_colleges()
    st.write("Colleges:")
    for college in colleges:
        st.write(f"College ID: {college['college_id']}, Name: {college['name']}, Type: {college['type']}, Address: {college['address']}")

elif display_universities_button:
    universities = display_universities()
    st.write("Universities:")
    for uni in universities:
        st.write(f"University ID: {uni['university_id']}, Name: {uni['university_name']}, Ranking: {uni['NIRF_ranking']}")
