"""
Exercise: Employee Management System

You are tasked with creating a simple Employee Management System. Each
employee will be represented as an "Employee" object with attributes such
as name, age, department, and salary.

Your task is to implement a Python program that allows users to perform the
following operations using a list of Employee objects:

Add an employee to the system.

Remove an employee from the system.

View all employees in the system.

python
"""

class Employee:
    def __init__(self, name, age, department, salary):
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary

def add_employee(employees, employee):
    employees.append(employee)
    print("Employee added successfully!")

def remove_employee(employees, employee_name):
    for emp in employees:
        if emp.name == employee_name:
            employees.remove(emp)
            print("Employee removed successfully!")
            break
    else:
        print("Employee not found!")

def view_employees(employees):
    if not employees:
        print("No employees in the system.")
        return
    
    print("List of Employees:")
    for idx, emp in enumerate(employees, start=1):
        print(f"{idx}. Name: {emp.name}, Age: {emp.age}, Department: {emp.department}, Salary: {emp.salary}")

def main():
    employees = []
    
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. View Employees")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter employee name: ")
            age = int(input("Enter employee age: "))
            department = input("Enter employee department: ")
            salary = float(input("Enter employee salary: "))
            new_employee = Employee(name, age, department, salary)
            add_employee(employees, new_employee)
        elif choice == "2":
            employee_name = input("Enter employee name to remove: ")
            remove_employee(employees, employee_name)
        elif choice == "3":
            view_employees(employees)
        elif choice == "4":
            print("Exiting the Employee Management System.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()

