# You have a list of students and their marks in three subjects. Build a report card generator by writing these functions:
# students = {
#     "Alice": [88, 92, 79],
#     "Bob": [55, 63, 70],
#     "Charlie": [95, 98, 100],
#     "Diana": [72, 68, 65]
# }
# 90 and above → "A"
# 80–89 → "B"
# 70–79 → "C"
# 60–69 → "D"
# Below 60 → "F"
# average
# grade
# print

students = {
    "Alice": [88, 92, 79],
    "Bob": [55, 63, 70],
    "Charlie": [95, 98, 100],
    "Diana": [72, 68, 65]
}

for student_name, marks_list in students.items():
    average = 0
    # average = (sum of marks in a subject) / len(subjects)
    sum_of_marks = 0
    for mark in marks_list:
        sum_of_marks = sum_of_marks + mark
    
    average = sum_of_marks / len(marks_list)

    # grade calculation
    if average >= 90:
        print(f"congrats {student_name}, you got an A")
    elif average >=80 and average < 90:
        print(f"congrats {student_name}, you got a B")
    elif average >=70 and average < 80:
        print(f"congrats {student_name}, you got a C")
    elif average >=60 and average < 70:
        print(f"congrats {student_name}, you got a D")
    else:
        print(f"{student_name}, you got an F")


    # print(student_name, marks_list)