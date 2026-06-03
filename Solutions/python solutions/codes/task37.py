class Employee:
    def __init__(self, emp_id, name, department):
        self.emp_id = emp_id
        self.name = name
        self.department = department
    def display_info(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Department: {self.department}")
emp1 = Employee(101, "Ravi", "IT")
emp2 = Employee(102, "Anita", "HR")
emp3 = Employee(103, "Kumar", "Finance")
employees = [emp1, emp2, emp3]
print("Employee Roster:")
for emp in employees:
    emp.display_info()
print("\nEmployee Names:")
for emp in employees:
    print(emp.name)