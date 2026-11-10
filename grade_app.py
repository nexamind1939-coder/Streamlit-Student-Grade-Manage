import streamlit as st

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Student Grade Manager",
    page_icon="🎓",
    layout="wide"
)

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
        return "F"


if "students" not in st.session_state:
    st.session_state.students = []

# HEADER
st.title("🎓 Student Grade Manager")

st.markdown(
    "Manage Student Marks and Academic Performance",
    text_alignment="center"
)

st.divider()


# --------------------------------
# ADD STUDENT FORM
# --------------------------------

st.subheader("➕ Add New Student")

with st.form("student_form", clear_on_submit=True):

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

    submit = st.form_submit_button("Add Student")

    if submit:

        if not name.strip():

            st.error("Please enter student name.")

        elif mark < 0 or mark > 100:

            st.error("Marks must be between 0 and 100.")

        else:

            student = {
                "Name": name.strip(),
                "Mark": int(mark),
                "Grade": get_grade(mark)
            }

            st.session_state.students.append(student)

            st.success(f"{name} added successfully!")


st.divider()


# --------------------------------
# DISPLAY STUDENT RESULTS
# --------------------------------

st.subheader("📋 Student Results")

if st.session_state.students:

    # Display table without Pandas

    st.table({
        "Name": [
            student["Name"]
            for student in st.session_state.students
        ],

        "Mark": [
            student["Mark"]
            for student in st.session_state.students
        ],

        "Grade": [
            student["Grade"]
            for student in st.session_state.students
        ]
    })

    st.divider()


    # --------------------------------
    # CLASS STATISTICS
    # --------------------------------

    st.subheader("📊 Class Performance")

    marks = [
        student["Mark"]
        for student in st.session_state.students
    ]

    average = sum(marks) / len(marks)

    highest = max(marks)

    lowest = min(marks)

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "📈 Average Marks",
        f"{average:.1f}"
    )

    col2.metric(
        "🏆 Highest Marks",
        highest
    )

    col3.metric(
        "📉 Lowest Marks",
        lowest
    )

    st.metric(
        "👨‍🎓 Total Students",
        len(st.session_state.students)
    )


    st.divider()


    # --------------------------------
    # CLEAR ALL STUDENTS
    # --------------------------------

    if st.button("🗑️ Clear All Students"):

        st.session_state.students = []

        st.rerun()

else:

    st.info("No students added yet. Please add a student.")


# --------------------------------
# FOOTER
# --------------------------------

st.divider()

st.markdown(
    "<center>🎓 Student Grade Manager | "
    "Built with Python and Streamlit</center>",
    unsafe_allow_html=True
)
