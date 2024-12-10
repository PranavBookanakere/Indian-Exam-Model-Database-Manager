import streamlit as st
import pandas as pd
import mysql.connector

# Create a connection to your MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='indian_exams'
)

# Function to fetch data from the PU_college table
def load_pu_colleges():
    cursor = conn.cursor()
    query = "SELECT * FROM PU_college"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])
    return df

# Function to insert a new PU college record into the database
def insert_pu_college(name, address, college_type, annual_fee, capacity, contact_email, contact_phone, college_description):
    cursor = conn.cursor()
    query = "INSERT INTO PU_college (name, address, type, annual_fee, capacity, contact_email, contact_phone, college_description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (name, address, college_type, annual_fee, capacity, contact_email, contact_phone, college_description)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()

# Main Streamlit app
def show_page():
    st.title("PU College Information")
    st.header("Add a New PU College")
    st.write("Welcome to the PU College page. Here, you can view and interact with PU College data.")

    with st.form("add_college_form"):
        name = st.text_input("Name")
        address = st.text_input("Address")
        college_type = st.selectbox("Type", ['Science', 'Commerce', 'Arts'])
        annual_fee = st.number_input("Annual Fee", value=0.0)
        capacity = st.number_input("Capacity", min_value=0)
        contact_email = st.text_input("Contact Email")
        contact_phone = st.text_input("Contact Phone")
        college_description = st.text_area("College Description")

        add_button = st.form_submit_button("Add College")

    if add_button:
        insert_pu_college(name, address, college_type, annual_fee, capacity, contact_email, contact_phone, college_description)
        st.success("College added successfully!")

    if st.button("View Added Colleges"):
        # Load data from the database
        pu_colleges = load_pu_colleges()

        if not pu_colleges.empty:
            # Display the data in a Streamlit DataFrame
            st.header("Added Colleges")
            st.dataframe(pu_colleges)
        else:
            st.warning("No colleges found in the database.")


# Entry point for the "PU College" page
if __name__ == '__main__':
    show_page()
