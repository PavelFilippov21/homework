from collections import Counter

students = [{'name': 'Вася'},
{'name': 'Петя'},
{'name': 'Маша'},
{'name': 'Маша'},
{'name': 'Петя'},
{'name': 'Петя'}]

stud_name = []

for student in students:
    stud_name.append(student["name"])

cound = Counter(stud_name).most_common(1)[0][0]
print(cound)