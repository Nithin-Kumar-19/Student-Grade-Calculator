# List to store (student_name, marks, grade, comment)
results = []


def calculate_grade(marks):
    if marks >= 90:
        return "A+", "Excellent work!"
    elif marks >= 80:
        return "A", "Great job!"
    elif marks >= 70:
        return "B", "Good effort."
    elif marks >= 60:
        return "C", "Satisfactory."
    elif marks >= 50:
        return "D", "Needs improvement."
    else:
        return "F", "Failed. Try harder."


def input_marks():
    while True:
        try:
            marks = float(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks should be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


# Main loop to take input for multiple students
while True:
    name = input("Enter student name (or 'exit' to stop): ").strip()
    if name.lower() == "exit":
        break

    marks = input_marks()
    grade, comment = calculate_grade(marks)

    results.append((name, marks, grade, comment))
    print(f"Student: {name}, Marks: {marks}, Grade: {grade}, Comment: {comment}\n")

# Display all results
print("\nAll Student Results:")
for student in results:
    print(f"Name: {student[0]}, Marks: {student[1]}, Grade: {student[2]}, Comment: {student[3]}")
