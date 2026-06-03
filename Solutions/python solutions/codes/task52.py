import json

gradebook = {}

def add_grade(student, grade):
    try:
        val = float(grade)
        if val < 0 or val > 100:
            raise ValueError
        if student not in gradebook:
            gradebook[student] = []
        gradebook[student].append(val)
    except ValueError:
        print("Invalid grade. Must be a number between 0 and 100.")

def calculate_gpa(student):
    if student not in gradebook or not gradebook[student]:
        return 0.0
    avg = sum(gradebook[student]) / len(gradebook[student])
    if avg >= 90:
        return 4.0
    elif avg >= 80:
        return 3.0
    elif avg >= 70:
        return 2.0
    elif avg >= 60:
        return 1.0
    else:
        return 0.0

def save_data(filename="grades.json"):
    with open(filename, "w") as f:
        json.dump(gradebook, f)

def load_data(filename="grades.json"):
    global gradebook
    try:
        with open(filename, "r") as f:
            gradebook = json.load(f)
    except FileNotFoundError:
        gradebook = {}

add_grade("kummu", "95")
add_grade("kummu", "88")
add_grade("ammu", "75")
add_grade("ammu", "abc")
save_data()
load_data()

for stu in gradebook:
    print(f"{stu} - Grades: {gradebook[stu]}, GPA: {calculate_gpa(stu)}")

all_grades = [g for grades in gradebook.values() for g in grades]
if all_grades:
    class_avg = sum(all_grades) / len(all_grades)
    print(f"Class Average: {class_avg:.2f}")
