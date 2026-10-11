import pandas as pd
import streamlit as st
from database import add_student, get_student, get_students
from services import calculate_grade, calculate_statistics

st.set_page_config(
    page_title="Student Performance Dashboard", layout="wide"
)

st.title("🎓 Student Performance Dashboard")

st.subheader("➕ Add New Student")

with st.form(key="add_student_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        student_name = st.text_input("Student Name")
    with col2:
        student_score = st.number_input(
            "Score", min_value=0.0, max_value=100.0, step=1.0
        )

    submit_button = st.form_submit_button(label="Add Student")

if submit_button:
    if student_name.strip():
        add_student(student_name.strip(), student_score)
        st.success(f"Tələbə '{student_name}' uğurla əlavə edildi!")
        st.rerun()
    else:
        st.error("Xahiş olunur tələbə adını daxil edin!")

st.divider()

all_students = get_students()

st.subheader("🔍 Search Student")
search_query = st.text_input("Search Student by Name")

if search_query.strip():
    display_students = get_student(search_query.strip())
else:
    display_students = all_students

formatted_students = []
for student in display_students:
    formatted_students.append(
        {
            "Name": student["name"],
            "Score": student["score"],
            "Grade": calculate_grade(student["score"]),
        }
    )

st.subheader("📊 Statistics")
stats = calculate_statistics(all_students)

m1, m2, m3, m4 = st.columns(4)
m1.metric("Total Students", stats["total_students"])
m2.metric("Average Score", stats["average_score"])
m3.metric("Highest Score", stats["highest_score"])
m4.metric("Lowest Score", stats["lowest_score"])

st.divider()

st.subheader("📋 Student List")
if formatted_students:
    df = pd.DataFrame(formatted_students)
    st.dataframe(df, use_container_width=True)
else:
    st.info("Heç bir tələbə tapılmadı.")