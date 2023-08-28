class Employee:
    def _init_(self, employee_id, name, age, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.salary = salary

    def _str_(self):
        return f"Employee ID: {self.employee_id}, Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

class EmployeeTable:
    def _init_(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def sort_by_age(self):
        self.employees.sort(key=lambda emp: emp.age)

    def sort_by_name(self):
        self.employees.sort(key=lambda emp: emp.name)

    def sort_by_salary(self):
        self.employees.sort(key=lambda emp: emp.salary)

    def display(self):
        for emp in self.employees:
            print(emp)

if _name_ == "_main_":
    employee_table = EmployeeTable()

    employee_data = [
        ("161E90", "Raman", 41, 56000),
        ("161F91", "Himadri", 38, 67500),
        ("161F99", "Jaya", 51, 82100),
        ("171E20", "Tejas", 30, 55000),
        ("171G30", "Ajay", 45, 44000)
    ]

    for emp_id, name, age, salary in employee_data:
        employee = Employee(emp_id, name, age, salary)
        employee_table.add_employee(employee)

    print("Sort by:\n1. Age\n2. Name\n3. Salary")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        employee_table.sort_by_age()
    elif choice == 2:
        employee_table.sort_by_name()
    elif choice == 3:
        employee_table.sort_by_salary()
    else:
        print("Invalid choice!")

    print("\nSorted Employee Data:")
    employee_table.display()