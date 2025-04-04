class person:
    def __init__(self):
        self.name="Gokul"
        self.age=24
class employee:
    def __init__(self):
        self.salary=10000
        self.department="Data Analyst"
call1=person()
call2=employee()
print("Name of the person: ",call1.name)
print("Department that he works: ",call2.department)