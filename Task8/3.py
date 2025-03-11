data = [
    {'Name': 'Alice', 'Age': 25, 'Salary': 50000, 'Department': 'HR'},
    {'Name': 'Bob', 'Age': None, 'Salary': 60000, 'Department': 'IT'},
    {'Name': 'Charlie', 'Age': 30, 'Salary': None, 'Department': 'Finance'},
    {'Name': 'David', 'Age': 35, 'Salary': 80000, 'Department': 'IT'},
    {'Name': 'Eve', 'Age': 40, 'Salary': 90000, 'Department': 'HR'}
]
for employee in data:
    if employee['Salary'] is not None:
        employee['Bonus'] = employee['Salary'] * 0.1
    else:
        employee['Bonus'] = None
print("The bonus added :",data)
for employee in data:
    if employee['Salary'] is None:
        print("salary is none")
    elif employee['Salary'] >  60000:
        print(employee)
    else:
        print("Input is less than 60000")