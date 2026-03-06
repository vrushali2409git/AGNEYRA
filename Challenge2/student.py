students = {}

while True:
    print("\nStudent Record System")
    print("1 Add Student")
    print("2 View Students")
    print("3 Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Enter student name: ")
        marks = input("Enter marks: ")
        students[name] = marks
        print("Student added")

    elif choice == '2':
        print("\nStudent List")
        for name, marks in students.items():
            print(name, "-", marks)

    elif choice == '3':
        print("Program closed")
        break

    else:
        print("Invalid choice")
