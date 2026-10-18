
print("===== STUDENT PERFORMANCE & PLACEMENT ANALYZER =====")

subjects = ["Maths", "Python", "English"]
students = []

while True:
    print("\n===== ENTER STUDENT DETAILS =====")

    name = input("Enter student name: ").strip()

    while not name:
        print("Name cannot be empty.")
        name = input("Enter student name: ").strip()

    marks = []

    for subject in subjects:
        while True:
            try:
                mark = int(input(f"Enter {subject} marks (0-100): "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Enter marks between 0 and 100.")

            except ValueError:
                print("Please enter numbers only.")

    # Get CGPA
    while True:
        try:
            cgpa = float(input("Enter CGPA (0-10): "))

            if 0 <= cgpa <= 10:
                break
            print("Enter CGPA between 0 and 10.")

        except ValueError:
            print("Enter a valid number.")

    # Get overall percentage
    while True:
        try:
            percentage = float(
                input("Enter overall percentage (0-100): ")
            )

            if 0 <= percentage <= 100:
                break
            print("Enter percentage between 0 and 100.")

        except ValueError:
            print("Enter a valid number.")

    # Get active backlogs
    while True:
        try:
            backlogs = int(input("Enter active backlogs: "))

            if backlogs >= 0:
                break
            print("Backlogs cannot be negative.")

        except ValueError:
            print("Enter a whole number.")

    # Analyze marks
    total = sum(marks)
    average = total / len(marks)

    highest_mark = max(marks)
    lowest_mark = min(marks)

    if any(mark < 35 for mark in marks):
        result = "Fail"
        grade = "F"
    else:
        result = "Pass"

        if average >= 90:
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

    # Demo placement criteria
    minimum_cgpa = 7.0
    minimum_percentage = 60.0
    maximum_backlogs = 0

    if (
        cgpa >= minimum_cgpa
        and percentage >= minimum_percentage
        and backlogs <= maximum_backlogs
    ):
        eligibility = "Eligible"
    else:
        eligibility = "Not Eligible"

    # Save student details
    students.append({
        "name": name,
        "marks": marks,
        "total": total,
        "average": average,
        "result": result,
        "grade": grade,
        "cgpa": cgpa,
        "percentage": percentage,
        "backlogs": backlogs,
        "eligibility": eligibility
    })

    choice = input(
        "\nAdd another student? (yes/no): "
    ).strip().lower()

    if choice not in ("yes", "y"):
        break

# Display combined report
print("\n===== COMBINED STUDENT REPORT =====")

for student in students:
    print("\n------------------------------")
    print("Student Name:", student["name"])

    for i, subject in enumerate(subjects):
        print(subject + " Marks:", student["marks"][i])

    print("Total Marks:", student["total"], "/ 300")
    print("Average:", round(student["average"], 2))
    print("Result:", student["result"])
    print("Grade:", student["grade"])

    marks = student["marks"]

    high_index = marks.index(max(marks))
    low_index = marks.index(min(marks))

    print(
        "Highest Marks:",
        subjects[high_index],
        "-",
        max(marks)
    )
    print(
        "Lowest Marks:",
        subjects[low_index],
        "-",
        min(marks)
    )

    print("\n--- Placement Details ---")
    print("CGPA:", student["cgpa"])
    print("Overall Percentage:", student["percentage"], "%")
    print("Active Backlogs:", student["backlogs"])
    print("Placement Status:", student["eligibility"])

# Find class topper
topper = max(students, key=lambda student: student["total"])

print("\n===== CLASS TOPPER =====")
print("Name:", topper["name"])
print("Total Marks:", topper["total"], "/ 300")
print("Average:", round(topper["average"], 2))
print("Grade:", topper["grade"])

# Placement summary
eligible_count = sum(
    1 for student in students
    if student["eligibility"] == "Eligible"
)

print("\n===== PLACEMENT SUMMARY =====")
print("Total Students:", len(students))
print("Eligible Students:", eligible_count)
print("Not Eligible Students:", len(students) - eligible_count)

print("\nAnalysis completed successfully!")
