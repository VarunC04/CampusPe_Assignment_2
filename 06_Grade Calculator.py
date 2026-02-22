# Q6: Grade Calculator
# This program collects marks for 5 subjects, calculates total, percentage, grade, and pass/fail status.

def grade_calculator():
    marks_list = []

    # Taking marks for 5 subjects with error handling
    for subject_number in range(1, 6):
        try:
            mark = float(input(f"Enter marks for subject {subject_number} (0–100): "))
            if mark < 0 or mark > 100:
                print("Marks must be between 0 and 100.")
                return
            marks_list.append(mark)
        except ValueError:
            print("Invalid input! Please enter a number.")
            return

    # Calculating basic results
    total_marks = sum(marks_list)
    percentage = (total_marks / 500) * 100
    passed_all = all(mark >= 40 for mark in marks_list)

    # Determining grade
    if percentage >= 90:
        grade = "A+ (Outstanding)"
    elif percentage >= 80:
        grade = "A (Excellent)"
    elif percentage >= 70:
        grade = "B (Good)"
    elif percentage >= 60:
        grade = "C (Average)"
    elif percentage >= 50:
        grade = "D (Pass)"
    else:
        grade = "F (Fail)"

    # Displaying final results
    print("Marks:", marks_list)
    print(f"Total Marks: {total_marks}/500")
    print(f"Percentage: {percentage:.2f}%")
    print("Grade:", grade)
    print("Result:", "Pass" if passed_all else "Fail")

grade_calculator()
