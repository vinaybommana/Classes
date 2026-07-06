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

def calculate_average(marks): # list
    sum = 0
    for mark in marks:
        sum = sum + mark
    average = sum / len(marks)
    return average # number


def calculate_grade(average): # number
    # grade calculation
    grade = "" # grade is global
    if average >= 90:
        grade = "A"
    elif average >=80 and average < 90:
        grade = "B"
    elif average >=70 and average < 80:
        grade = "C"
    elif average >=60 and average < 70:
        grade = "D"
    else:
        grade = "E"
    return grade # string


def calculate_percentage(marks): # marks is a list
    # percentage
    sum = 0
    for mark in marks:
        sum = sum + mark
    
    percentage = sum / (100 * len(marks)) * 100
    return percentage


def generate_report(student, students): # student is a string input
    print("----------------------")
    print(f"Hey {student}, Congrats")
    marks_list = students[student] # accessing value
    average = calculate_average(marks_list)
    grade = calculate_grade(average)
    percentage = calculate_percentage(marks_list)
    print(f"you got an {grade}")
    print(f"you got {percentage}")
    print("----------------------")


students = {
    "Alice": [88, 92, 79],
    "Bob": [55, 63, 70],
    "Charlie": [95, 98, 100],
    "Diana": [72, 68, 65]
}

generate_report("Bob", students)