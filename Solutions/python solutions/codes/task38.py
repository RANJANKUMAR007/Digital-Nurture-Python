class Employee:
    def __init__(self, name):
        self.name = name
        self.salary = 0
    def set_salary(self, salary):
        # Validate salary
        if isinstance(salary, (int, float)) and salary >= 0:
            self.salary = salary
        else:
            print("Invalid salary amount.")
        return self 

    def apply_raise(self, raise_amount):
        if isinstance(raise_amount, (int, float)) and raise_amount >= 0:
            self.salary += raise_amount
        else:
            print("Invalid raise amount.")
        return self  
    def display_salary(self):
        print(f"Final Salary of {self.name}: {self.salary}")
        return self  # Return self for method chaining
employee = Employee("Ravi")
employee.set_salary(50000).apply_raise(5000).display_salary()