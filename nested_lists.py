# https://www.hackerrank.com/challenges/nested-list/problem
students = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

students_study_harder = []

# If there are two people with the same grade, print both students
student_dict = {row[0]: row[1] for row in students for k in row[1:]}
smallest_score = min(student_dict.values())
new_student_dict = {k: v for k, v in student_dict.items() if v != smallest_score}

for student, grade in new_student_dict.items():
    # Add each student to student study list
    if len(students_study_harder) == 0:
        students_study_harder.append([student, grade])
    if grade < students_study_harder[0][1]:
        students_study_harder.pop(0)
        students_study_harder.append([student, grade])
    # If student in study list the same as student grade, add to study list
    if grade == students_study_harder[0][1] and student != students_study_harder[0][0]:
        students_study_harder.append([student, grade])

for students in sorted(students_study_harder):
    print(students[0])


