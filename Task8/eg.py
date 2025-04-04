# student_data = {
#     "name": "John",
#     "age": 26,
#     "courses": ["Math", "Physics", "Computer Science"],
#     "grades": {"Math": 85, "Physics": 90, "Computer Science": 95},
#     "attendance": 92.5
# }
# # print(student_data["courses"])
# # print(student_data["grades"]["Computer Science"])
# total=0
# for grade,value in student_data["grades"].items():
#     if grade!="Physics":
#         total+=value
# print(total)
company_data = {
    "company_name": "Tech Innovators",
    "employees": [
        {"id": 101, "name": "Alice", "role": "Developer", "salary": 70000, "skills": ["Python", "Django", "React"]},
        {"id": 102, "name": "Bob", "role": "Designer", "salary": 60000, "skills": ["Figma", "Photoshop"]},
        {"id": 103, "name": "Charlie", "role": "Manager", "salary": 90000, "skills": ["Leadership", "Finance"]},
        {"id": 104, "name": "David", "role": "Developer", "salary": 75000, "skills": ["Java", "Spring Boot", "Docker"]}
    ],
    "departments": {
        "Engineering": {"head": "Alice", "budget": 500000},
        "Design": {"head": "Bob", "budget": 300000},
        "Management": {"head": "Charlie", "budget": 400000}
    },
    "company_revenue": 2000000
}
for employee in company_data["employees"]:
    if len(employee["skills"])==3:
        print(employee["name"])
