import json

students = {}

def add_student(student_id, student_name):
    if student_id in students:
        raise ValueError(f"Student ID {student_id} already exists.")
    students[student_id] = {'name': student_name, 'grades': []}
    print(f"Student {student_name} added successfully.")

def record_grade(student_id, grade):
    if student_id not in students:
        raise ValueError(f"Student ID {student_id} does not exist.")
    if not isinstance(grade, (int, float)) or not (0 <= grade <= 100):
        raise ValueError("Grade must be a number between 0 and 100.")
    students[student_id]['grades'].append(grade)
    print(f"Grade {grade} recorded for student {students[student_id]['name']}.")

def calculate_average(student_id):
    if student_id not in students:
        raise ValueError(f"Student ID {student_id} does not exist.")
    grades = students[student_id]['grades']
    if not grades:
        return 0
    average = sum(grades) / len(grades)
    print(f"Average grade for student {students[student_id]['name']} is {average:.2f}.")
    return average

def sort_students_by_average():
    sorted_students = sorted(students.items(), key=lambda item: calculate_average(item[0]), reverse=True)
    print("Students sorted by average grades:")
    for student_id, info in sorted_students:
        print(f"{info['name']}: {calculate_average(student_id):.2f}")

def export_data(filename):
    with open(filename, 'w') as file:
        json.dump(students, file, indent=4)
    print(f"Data exported to {filename}.")

def import_data(filename):
    global students
    try:
        with open(filename, 'r') as file:
            students = json.load(file)
        print(f"Data imported from {filename}.")
    except FileNotFoundError:
        print(f"File {filename} not found.")

def main():
    while True:
        print("\nStudent Grade Management System")
        print("1. Add Student")
        print("2. Record Grade")
        print("3. Calculate Average")
        print("4. Sort Students by Average")
        print("5. Export Data")
        print("6. Import Data")
        print("7. Exit")
        
        choice = input("Choose an option: ")
        
        try:
            if choice == '1':
                student_id = input("Enter student ID: ")
                student_name = input("Enter student name: ")
                add_student(student_id, student_name)
            elif choice == '2':
                student_id = input("Enter student ID: ")
                grade = float(input("Enter grade: "))
                record_grade(student_id, grade)
            elif choice == '3':
                student_id = input("Enter student ID: ")
                calculate_average(student_id)
            elif choice == '4':
                sort_students_by_average()
            elif choice == '5':
                filename = input("Enter filename to export data: ")
                export_data(filename)
            elif choice == '6':
                filename = input("Enter filename to import data: ")
                import_data(filename)
            elif choice == '7':
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please choose a valid option.")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
