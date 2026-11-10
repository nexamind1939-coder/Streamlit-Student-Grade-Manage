
import streamlit as st
import pandas as pd

# --------------------------------
# PAGE CONFIGURATION
# --------------------------------

st.set_page_config(
    page_title="Student Grade Manager",
    page_icon="🎓",
    layout="wide"
)

# --------------------------------
# CUSTOM CSS
# --------------------------------

st.markdown("""
<style>
    .main {
        background-color: #f5f7fb;
    }

    .title {
        text-align: center;
        color: #283593;
        font-size: 40px;
        font-weight: bold;
    }

    .subtitle {
        text-align: center;
        color: #666666;
        font-size: 17px;
    }

    .stButton button {
        background-color: #3949ab;
        color: white;
        border-radius: 10px;
        height: 45px;
        font-weight: bold;
        width: 100%;
    }

    .stButton button:hover {
        background-color: #1a237e;
        color: white;
    }
</style>
""", unsafe_allow_html=True)


# --------------------------------
# SESSION STATE
# --------------------------------

if "students" not in st.session_state:
    st.session_state.students = []


# --------------------------------
# GRADING FUNCTION
# --------------------------------

def get_grade(mark):

    if mark >= 90:
        return "A"

    elif mark >= 80:
        return "B"

    elif mark >= 70:
        return "C"

    elif mark >= 60:
        return "D"

    else:
        return "E"


# --------------------------------
# PAGE HEADER
# --------------------------------

st.markdown(
    '<div class="title">🎓 Student Grade Manager</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Manage student marks, grades and class performance</div>',
    unsafe_allow_html=True
)

st.divider()


# --------------------------------
# ADD STUDENT FORM
# --------------------------------

st.subheader("➕ Add New Student")

with st.form("add_student_form", clear_on_submit=True):

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input(
            "Student Name",
            placeholder="Enter student name"
        )

    with col2:
        mark = st.number_input(
            "Student Mark",
            min_value=0,
            max_value=100,
            value=0,
            step=1
        )

    submitted = st.form_submit_button(
        "➕ Add Student"
    )

    if submitted:

        if not name.strip():

            st.error("Please enter a student name.")

        elif not 0 <= mark <= 100:

            st.error("Mark must be between 0 and 100.")

        else:

            grade = get_grade(mark)

            student = {
                "Name": name.strip(),
                "Mark": int(mark),
                "Grade": grade
            }

            st.session_state.students.append(student)

            st.success(
                f"{name.strip()} added successfully! Grade: {grade}"
            )


st.divider()


# --------------------------------
# STUDENT RESULTS TABLE
# --------------------------------

st.subheader("📋 Student Results")

if st.session_state.students:

    df = pd.DataFrame(st.session_state.students)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # --------------------------------
    # CLASS STATISTICS
    # --------------------------------

    st.subheader("📊 Class Performance")

    marks = [student["Mark"]
             for student in st.session_state.students]

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "📈 Class Average",
        f"{average:.1f}"
    )

    col2.metric(
        "🏆 Highest Mark",
        highest
    )

    col3.metric(
        "📉 Lowest Mark",
        lowest
    )

    st.divider()

    # --------------------------------
    # TOTAL STUDENTS
    # --------------------------------

    st.subheader("👥 Class Information")

    st.metric(
        "Total Students",
        len(st.session_state.students)
    )

    # --------------------------------
    # CLEAR ALL STUDENTS
    # --------------------------------

    if st.button("🗑️ Clear All Students"):

        st.session_state.students = []

        st.rerun()

else:

    st.info(
        "No students added yet. "
        "Use the form above to add your first student."
    )


# --------------------------------
# FOOTER
# --------------------------------

st.divider()

st.markdown(
    "<center>Student Grade Manager | Built with Python & Streamlit</center>",
    unsafe_allow_html=True
)
