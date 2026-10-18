

print("===== STUDENT MARKS ANALYZER =====")

name = input("Enter student name: ")

subjects = ["Maths", "Python", "English"]
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
highest_mark = max(marks)
lowest_mark = min(marks)

highest_subject = subjects[marks.index(highest_mark)]
lowest_subject = subjects[marks.index(lowest_mark)]
average = total / len(marks)

print("\n===== RESULT =====")
print("Student Name:", name)
print("Total Marks:", total, "/ 300")
print("Average:", round(average, 2))

if any(mark < 35 for mark in marks):
    result = "Fail"
elif average >= 40:
    result = "Pass"
else:
    result = "Fail"

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

print("Result:", result)
print("Grade:", grade)
print("Highest Marks:", highest_subject, "-", highest_mark)
print("Lowest Marks:", lowest_subject, "-", lowest_mark)
