import streamlit as st
from pages import PU_College, University, Exams, Student_Registration, Results, Eligible_PU_Colleges, Eligible_Universities, Shortlist_students

st.set_page_config(
    page_title='MULTI PAGES WEB APP',
    page_icon="***"
)

def show_page():
    st.title("📚 Educational Database Web App 🎓")
    
    st.markdown(
        """
        <div style="background-color: #f2f2f2; padding: 10px; border-radius: 10px; color: black">
            <p>Welcome to our <strong>Educational Database Web App</strong>! 🚀</p>
            <p>Explore student information, colleges, universities, exams, results, and more! 📖</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write(
        """
        <div style="background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 3px 3px 5px 6px #ccc; color: black">
            <p>Our web app is your gateway to a world of knowledge and learning. 🌍</p>
            <p>Whether you're a <strong>student</strong>, a <strong>parent</strong>, or an <strong>educator</strong>, we're here to provide you with the educational resources you need. 🤓</p>
            <p>Discover a treasure trove of information on <em>students</em>, <em>colleges</em>, <em>universities</em>, <em>exams</em>, <em>enrollments</em>, <em>results</em>, and <em>scholarships</em>. 🎓</p>
            <p>Get ready to embark on an exciting educational journey with us! 🌟</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Key Features 🌟")
    st.markdown(
        "- 📜 View student information and academic performance."
        "\n- 🏫 Explore PU colleges, universities, exams, and tuition centers."
        "\n- 📊 Check exam results, admission details, and scholarships."
        "\n- 🔍 User-friendly search and filter options for easy access to data."
    )

    st.write("Ready to dive into the world of education? Use the sidebar on the left to navigate through various sections of the app.")
    #st.write(sys.executable)

# Entry point for the homepage
if __name__ == '__main__':
    show_page()
