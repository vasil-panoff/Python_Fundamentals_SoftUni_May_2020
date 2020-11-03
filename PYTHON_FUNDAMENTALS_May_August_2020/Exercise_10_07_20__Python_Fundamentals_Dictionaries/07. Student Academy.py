n = int(input())

students = {}

for i in range(n):
    student_name = input()
    grade = float(input())

    if student_name not in students:
        students[student_name] = []

    students[student_name].append(grade)

students_average_results = {}

for student, grade in students.items():
    average = sum(grade) / len(grade)

    if average < 4.5:
        continue

    students_average_results[student] = average

students_average_results = dict(sorted(students_average_results.items(), key= lambda x: x[1], reverse=True))


for student, avrg in students_average_results.items():
    print(f"{student} -> {avrg:.2f}")
