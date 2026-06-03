class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, emp_string):
        # Parse and validate string input
        try:
            name, salary = emp_string.split(",")
            salary = int(salary)  # Convert salary to integer
            return cls(name, salary)  # Create and return object
        except ValueError:
            print("Invalid input format. Use: Name,Salary")
            return None

    def display_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Salary: {self.salary}")


emp = Employee.from_string("Shubh,75000")
if emp:
    emp.display_details()