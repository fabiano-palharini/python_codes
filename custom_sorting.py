employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

employees.sort(key=lambda employee: employee['age'])
print(employees)

employees.sort(key=lambda employee: employee.get('salary'), reverse=True)
print(employees)

zxc = sorted(employees, key=lambda employee: employee.get('age'),reverse=True)
print(zxc)

print(zxc[0])
print(zxc[0]['Name'])
print(zxc[0].get('age'))

zxc[0]['age'] = 41
print(zxc[0])

#invalid
# zxc[0].get('age') = 42
# print(zxc[0])

print(employees)  #copia por referencia