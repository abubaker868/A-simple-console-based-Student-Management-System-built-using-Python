students = []

def add_student():
    try:
        name = input("Enter student name: ")
        age = int(input("Enter age: "))
        roll = int(input("Enter roll number: "))
        
        student = {
            "name": name,
            "age": age,
            "roll": roll
        }

        students.append(student)
        print("Student added successfully!\n")
    except ValueError:
        print("Invalid input! Age and roll must be numbers.\n")

def view_students():
    if not students:
        print("No students found.\n")  
    else:
        print("\n--- Student List ---")
        for s in students:
            print(f"Name: {s['name']}, Age: {s['age']}, Roll: {s['roll']}")
        print()

def search_student():
    try:
        roll = int(input("Enter roll number to search: "))
        for s in students:
            if s["roll"] == roll:
                print(f"\nStudent Found: Name: {s['name']}, Age: {s['age']}, Roll: {s['roll']}\n")
                return
        print("Student not found.\n")
    except ValueError:
        print("Invalid input! Roll number must be a number.\n")

def delete_student():
    try:
        roll = int(input("Enter roll number to delete: "))
        for s in students:
            if s["roll"] == roll:
                students.remove(s)
                print("Student deleted successfully.\n")
                return
        print("Student not found.\n")
    except ValueError:
        print("Invalid input! Roll number must be a number.\n")

def main():
    while True:
        print("--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-5): "))
            print()  # Just for spacing

            if choice == 1:
                add_student()
            elif choice == 2:
                view_students()
            elif choice == 3:
                search_student()
            elif choice == 4:
                delete_student()
            elif choice == 5:
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")
        except ValueError:
            print("Please enter a valid number.\n")

if __name__ == "__main__":
    main()

