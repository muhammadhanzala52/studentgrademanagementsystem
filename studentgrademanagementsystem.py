import json

# Dictionary to store student data
students = {}

# Function to add a new student
def add_student(student_id, student_name):
    if student_id in students:
        raise ValueError(f"Student ID {student_id} already exists.")  # Check for duplicate student ID
    students[student_id] = {'name': student_name, 'grades': []}  # Add student with empty grades list
    print(f"Student {student_name} added successfully.")

# Function to record a grade for a student
def record_grade(student_id, grade):
    if student_id not in students:
        raise ValueError(f"Student ID {student_id} does not exist.")  # Check if student ID exists
    students[student_id]['grades'].append(grade)  # Append the grade to the student's grades list
    print(f"Grade {grade} recorded for student {students[student_id]['name']}.")

# Function to calculate the average grade for a student
def calculate_average(student_id):
    if student_id not in students:
        raise ValueError(f"Student ID {student_id} does not exist.")  # Check if student ID exists
    grades = students[student_id]['grades']
    if not grades:
        return 0  # Return 0 if there are no grades
    average = sum(grades) / len(grades)  # Calculate the average grade
    print(f"Average grade for student {students[student_id]['name']} is {average:.2f}.")
    return average

# Function to sort students by their average grade in descending order
def sort_students_by_average():
    sorted_students = sorted(students.items(), key=lambda item: calculate_average(item[0]), reverse=True)
    print("Students sorted by average grades:")
    for student_id, info in sorted_students:
        print(f"{info['name']}: {calculate_average(student_id):.2f}")

# Function to export student data to a JSON file
def export_data(filename):
    with open(filename, 'w') as file:
        json.dump(students, file, indent=4)  # Dump the students dictionary to a JSON file
    print(f"Data exported to {filename}.")

# Function to import student data from a JSON file
def import_data(filename):
    global students
    try:
        with open(filename, 'r') as file:
            students = json.load(file)  # Load the JSON data into the students dictionary
        print(f"Data imported from {filename}.")
    except FileNotFoundError:
        print(f"File {filename} not found.")  # Handle file not found error

# Main function to run the student grade management system
def main():
    while True:
        # Display the menu
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
                # Add a new student
                student_id = input("Enter student ID: ")
                student_name = input("Enter student name: ")
                add_student(student_id, student_name)
            elif choice == '2':
                # Record a grade for a student
                student_id = input("Enter student ID: ")
                try:
                    grade = float(input("Enter grade: "))
                    if not (0 <= grade <= 100):
                        raise ValueError  # Raise error if grade is not between 0 and 100
                    record_grade(student_id, grade)
                except ValueError:
                    print("Please enter a valid number between 0 and 100.")  # Handle invalid grade input
            elif choice == '3':
                # Calculate and display the average grade for a student
                student_id = input("Enter student ID: ")
                calculate_average(student_id)
            elif choice == '4':
                # Sort students by their average grade
                sort_students_by_average()
            elif choice == '5':
                # Export student data to a file
                filename = input("Enter filename to export data: ")
                export_data(filename)
            elif choice == '6':
                # Import student data from a file
                filename = input("Enter filename to import data: ")
                import_data(filename)
            elif choice == '7':
                # Exit the system
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please choose a valid option.")  # Handle invalid menu choice
        except ValueError as e:
            print(f"Error: {e}")  # Handle general value errors

if __name__ == "__main__":
    main()
