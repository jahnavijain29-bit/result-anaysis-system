# Result Analysis System

# Number of students
n = int(input("Enter number of students: "))

students = []

for i in range(n):
    print(f"\nEnter details of student {i+1}")
    name = input("Name: ")

    marks = []
    subjects = int(input("Enter number of subjects: "))

    for j in range(subjects):
        mark = int(input(f"Enter marks for subject {j+1}: "))
        marks.append(mark)

    total = sum(marks)
    percentage = total / subjects

    # Result
    if percentage >= 40:
        result = "Pass"
    else:
        result = "Fail"

    # Grade
    if percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    students.append({
        "name": name,
        "total": total,
        "percentage": percentage,
        "result": result,
        "grade": grade
    })

# ----------- Analysis -----------
percentages = [s["percentage"] for s in students]

print("\n📊 RESULT ANALYSIS REPORT 📊")
print("-" * 40)

for s in students:
    print(f"Name: {s['name']}")
    print(f"Total Marks: {s['total']}")
    print(f"Percentage: {s['percentage']:.2f}%")
    print(f"Result: {s['result']}")
    print(f"Grade: {s['grade']}")
    print("-" * 40)

print("Class Average Percentage:", sum(percentages) / n)
print("Highest Percentage:", max(percentages))
print("Lowest Percentage:", min(percentages))
