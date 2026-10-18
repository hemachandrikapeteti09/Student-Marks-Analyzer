
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
average = total / len(marks)

print("\n===== RESULT =====")
print("Student Name:", name)
print("Total Marks:", total, "/ 300")
print("Average:", round(average, 2))

if any(mark < 35 for mark in marks):
    print("Result: Fail")
elif average >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")
