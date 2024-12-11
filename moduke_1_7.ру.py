grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
student_grades = dict()
sorted_student_grades = sorted(student_grades.items(), key=lambda x: x[0])
for i, name in enumerate(students):
    student_grades[name] = sum(grades[i]) / len(grades[i])
print(dict(sorted_student_grades))
print(student_grades)