
# 🎓 Student Marks Analyzer

A Python-based project to analyze student marks, calculate academic performance, assign grades, and identify the class topper.

## 📌 About the Project

Student Marks Analyzer is a beginner-friendly Python application that evaluates students' academic performance in three subjects: Maths, Python, and English.

The program calculates total marks and average marks, determines Pass or Fail status, assigns grades, displays the highest and lowest subject marks, and identifies the class topper based on total marks.

## ✨ Features

- **Multiple Student Analysis:** Enter and analyze details for multiple students.
- **Total Marks Calculation:** Calculates total marks out of 300.
- **Average Calculation:** Computes the average marks for each student.
- **Pass/Fail Result:** A student passes only if they score at least 35 marks in every subject.
- **Automatic Grade Assignment:** Assigns grades based on the student's average.
- **Highest Subject Marks:** Displays the subject in which the student scored the highest marks.
- **Lowest Subject Marks:** Displays the subject in which the student scored the lowest marks.
- **Class Topper Identification:** Finds the student with the highest total marks.
- **Input Validation:** Prevents invalid marks and handles non-numeric input.
- **Student Result Report:** Displays each student's marks, total, average, result, and grade.

## 🏆 Grading System

| Average Marks | Grade |
|---|---|
| 90–100 | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| Below 50 | E |
| Failed in any subject | F |

**Note:** Students scoring below 35 in any subject receive an F grade.

## 🛠️ Technologies Used

- Python 3
- Lists and dictionaries
- Loops and conditional statements
- Functions such as `sum()`, `max()`, and `min()`
- Exception handling
- User input and output

## ▶️ How to Run

1. Install Python 3 on your computer.
2. Download or clone this repository.
3. Open the project folder in VS Code or a terminal.
4. Run the following command:

```bash
python marks_analyzer.py
```

5. Enter the student name and marks for Maths, Python, and English.
6. Choose whether to add another student.
7. View all student results and the class topper.

## 💻 Sample Output

```text
===== ALL STUDENT RESULTS =====

Student Name: Ravi
Total Marks: 270 / 300
Average: 90.0
Result: Pass
Grade: A+
Highest Marks: Maths - 95
Lowest Marks: English - 85

===== CLASS TOPPER =====
Name: Ravi
Total Marks: 270 / 300
Average: 90.0
```

*Sample values are for illustration; actual results depend on the marks entered.*

## 🎯 Learning Outcomes

- Practiced Python programming fundamentals.
- Learned to store and process multiple students' data.
- Applied validation and exception handling.
- Implemented academic grading logic.
- Compared student performance to identify the class topper.

## 👩‍💻 Author

**Hemachandrika**

---

*This project was developed as a Python programming learning project.*
