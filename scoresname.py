from collections import Counter

students = [{'name': 'Вася'},
{'name': 'Петя'},
{'name': 'Маша'},
{'name': 'Маша'},
{'name': 'Петя'},]

stud_names = []

for student in students:
    print(student)
    print(student['name'])
    stud_names.append(student['name'])

print(stud_names)
count = Counter(stud_names)
print(count)
