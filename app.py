
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Student Performance & Placement Analyzer",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student Performance & Placement Analyzer")
st.caption("Analyze student marks, academic performance and placement eligibility.")

if "students" not in st.session_state:
    st.session_state.students = []

st.subheader("📝 Enter Student Details")

with st.form("student_form"):
    name = st.text_input("Student Name")

    st.markdown("#### Subject Marks (0–100)")
    c1, c2, c3 = st.columns(3)

    with c1:
        maths = st.number_input("Maths", 0, 100, 0)
    with c2:
        python_marks = st.number_input("Python", 0, 100, 0)
    with c3:
        english = st.number_input("English", 0, 100, 0)

    st.markdown("#### Academic & Placement Details")
    c4, c5 = st.columns(2)

    with c4:
        cgpa = st.number_input(
            "CGPA (0–10)",
            min_value=0.0,
            max_value=10.0,
            value=8.5,
            step=0.1
        )

    with c5:
        backlogs = st.number_input(
            "Active Backlogs",
            min_value=0,
            max_value=100,
            value=0,
            step=1
        )

    submitted = st.form_submit_button(
        "Analyze Student",
        use_container_width=True
    )

if submitted:
    if not name.strip():
        st.error("Please enter the student name.")
    else:
        marks = [maths, python_marks, english]
        total = sum(marks)
        average = total / len(marks)

        # Percentage is automatically calculated from subject marks
        percentage = average

        result = "Fail" if any(m < 35 for m in marks) else "Pass"

        if result == "Fail":
            grade = "F"
        elif average >= 90:
            grade = "A+"
        elif average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "E"

        # Check each placement condition separately
        cgpa_ok = cgpa >= 7.0
        percentage_ok = percentage >= 60.0
        backlogs_ok = backlogs == 0

        eligible = cgpa_ok and percentage_ok and backlogs_ok
        eligibility = "Eligible" if eligible else "Not Eligible"

        student = {
            "Student Name": name.strip(),
            "Maths": maths,
            "Python": python_marks,
            "English": english,
            "Total": total,
            "Average": round(average, 2),
            "Result": result,
            "Grade": grade,
            "CGPA": round(cgpa, 2),
            "Percentage": round(percentage, 2),
            "Backlogs": backlogs,
            "Placement Status": eligibility
        }

        # Replace existing record if the name matches
        st.session_state.students = [
            s for s in st.session_state.students
            if s["Student Name"].casefold()
            != name.strip().casefold()
        ]
        st.session_state.students.append(student)

        st.success(f"Analysis completed for {name.strip()}!")

if st.session_state.students:
    students = st.session_state.students

    st.divider()
    st.header("📊 Student Performance Report")

    selected_name = st.selectbox(
        "Select student to view report",
        [s["Student Name"] for s in students]
    )

    student = next(
        s for s in students
        if s["Student Name"] == selected_name
    )

    st.subheader(f"Results: {student['Student Name']}")

    a, b, c, d = st.columns(4)
    a.metric("Total Marks", f"{student['Total']} / 300")
    b.metric("Average / Percentage", f"{student['Percentage']}%")
    c.metric("Grade", student["Grade"])
    d.metric("Result", student["Result"])

    st.markdown("#### Subject-wise Marks")
    st.dataframe(
        pd.DataFrame({
            "Subject": ["Maths", "Python", "English"],
            "Marks": [
                student["Maths"],
                student["Python"],
                student["English"]
            ]
        }),
        hide_index=True,
        use_container_width=True
    )

    subject_marks = {
        "Maths": student["Maths"],
        "Python": student["Python"],
        "English": student["English"]
    }

    highest = max(subject_marks, key=subject_marks.get)
    lowest = min(subject_marks, key=subject_marks.get)

    x, y = st.columns(2)
    x.info(f"🏆 Highest Marks: {highest} — {subject_marks[highest]}")
    y.info(f"📉 Lowest Marks: {lowest} — {subject_marks[lowest]}")

    st.subheader("💼 Placement Analysis")

    p1, p2, p3 = st.columns(3)
    p1.metric("CGPA", f"{student['CGPA']} / 10")
    p2.metric("Overall Percentage", f"{student['Percentage']}%")
    p3.metric("Active Backlogs", student["Backlogs"])

    if student["Placement Status"] == "Eligible":
        st.success("✅ Placement Status: Eligible")
    else:
        st.warning("⚠️ Placement Status: Not Eligible")
        st.write("Conditions to qualify:")

        st.write(
            f"{'✅' if student['CGPA'] >= 7.0 else '❌'} "
            "CGPA must be at least 7.0"
        )
        st.write(
            f"{'✅' if student['Percentage'] >= 60.0 else '❌'} "
            "Percentage must be at least 60%"
        )
        st.write(
            f"{'✅' if student['Backlogs'] == 0 else '❌'} "
            "Active backlogs must be zero"
        )

    st.caption(
        "Demo criteria only. Actual company placement rules may differ. "
        "Percentage is calculated from the three subject marks entered."
    )

    st.divider()
    st.header("🏆 Class Topper")

    topper = max(students, key=lambda s: s["Total"])

    t1, t2, t3 = st.columns(3)
    t1.metric("Topper Name", topper["Student Name"])
    t2.metric("Topper Total", f"{topper['Total']} / 300")
    t3.metric("Topper Average", f"{topper['Average']}%")

    st.header("📋 Combined Student Report")
    st.dataframe(
        pd.DataFrame(students),
        hide_index=True,
        use_container_width=True
    )

    eligible_count = sum(
        s["Placement Status"] == "Eligible"
        for s in students
    )

    st.header("📈 Placement Summary")
    q1, q2, q3 = st.columns(3)
    q1.metric("Total Students", len(students))
    q2.metric("Eligible Students", eligible_count)
    q3.metric("Not Eligible", len(students) - eligible_count)

    if st.button("Clear All Student Records"):
        st.session_state.students = []
        st.rerun()
else:
    st.info(
        "Enter student details above and click Analyze Student "
        "to view results."
    )
