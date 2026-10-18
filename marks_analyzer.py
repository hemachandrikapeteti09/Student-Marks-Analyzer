
print("===== STUDENT MARKS ANALYZER =====")

subjects = ["Maths", "Python", "English"]
students = []

while True:
    name = input("\nEnter student name: ").strip()

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
                    print("Invalid marks! Enter marks from 0 to 100.")

            except ValueError:
                print("Please enter numbers only.")

    total = sum(marks)
    average = total / len(marks)
    highest_mark = max(marks)
    lowest_mark = min(marks)

    highest_subject = subjects[marks.index(highest_mark)]
    lowest_subject = subjects[marks.index(lowest_mark)]

    if any(mark < 35 for mark in marks):
        result = "Fail"
    else:
        result = "Pass"

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

    student = {
        "name": name,
        "marks": marks,
        "total": total,
        "average": average,
        "result": result,
        "grade": grade
    }

    students.append(student)

    choice = input("\nAdd another student? (yes/no): ").strip().lower()

    if choice not in ("yes", "y"):
        break

print("\n===== ALL STUDENT RESULTS =====")

for student in students:
    print("\nStudent Name:", student["name"])
    print("Total Marks:", student["total"], "/ 300")
    print("Average:", round(student["average"], 2))
    print("Result:", student["result"])
    print("Grade:", student["grade"])

    marks = student["marks"]
    print("Highest Marks:", subjects[marks.index(max(marks))], "-", max(marks))
    print("Lowest Marks:", subjects[marks.index(min(marks))], "-", min(marks))

topper = max(students, key=lambda student: student["total"])

print("\n===== CLASS TOPPER =====")
print("Name:", topper["name"])
print("Total Marks:", topper["total"], "/ 300")
print("Average:", round(topper["average"], 2))
