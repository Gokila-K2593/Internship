students = {} 
while True:
    print("\n1. Add Student\n2. Delete Student\n3. Search Student\n4. Display All Students\n5. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter student marks: "))
        students[name] = marks
        print("Student added!")
    elif choice == "2":
        name = input("Enter student name to delete: ")
        if students.pop(name, None):
            print("Student deleted!")
        else:
            print("Student not found!")
    elif choice == "3":
        name = input("Enter student name to search: ")
        print(name,":",students.get(name,'Not found'))
    elif choice == "4":
        for name, marks in sorted(students.items(), key=lambda x: x[1], reverse=True):
            print(name,":",marks)
    elif choice == "5":
        print("Exiting")
        break
    else:
        print("Invalid choice! Try again.")