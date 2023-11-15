import streamlit as st
import pandas as pd
import mysql.connector

# Create a connection to your MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='16020byaadav',
    database='indian_exams'
)

# Function to fetch data from the UNIVERSITY table
def load_universities():
    cursor = conn.cursor()
    query = "SELECT * FROM UNIVERSITY"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])
    return df

# Function to insert a new University record into the database
def insert_university(campus, annual_fee, location, capacity, NIRF_ranking, university_name):
    cursor = conn.cursor()
    query = "INSERT INTO UNIVERSITY (campus, annual_fee, location, capacity, NIRF_ranking, university_name) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (campus, annual_fee, location, capacity, NIRF_ranking, university_name)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()



# Main Streamlit app
def show_page():
    st.title("University Information")
    st.header("Add a New University")
    st.write("Welcome to the University page. Here, you can view and interact with University data.")

    with st.form("add_university_form"):
        university_name = st.text_input("University Name")
        campus = st.text_input("Campus")
        annual_fee = st.number_input("Annual Fee", value=0.0)
        location = st.text_input("Location")
        capacity = st.number_input("Capacity", min_value=0)
        NIRF_ranking = st.number_input("NIRF Ranking")

        add_button = st.form_submit_button("Add University")

        st.empty()

    if add_button:
        insert_university(campus, annual_fee, location, capacity, NIRF_ranking, university_name)
        st.success("University added successfully!")

    if st.button("View Added Universities"):
        # Load data from the database
        universities = load_universities()

        if not universities.empty:
            # Display the data in a Streamlit DataFrame
            st.header("Added Universities")
            st.dataframe(universities)
        else:
            st.warning("No universities found in the database.")


# Entry point for the "University" page
if __name__ == '__main__':
    show_page()
