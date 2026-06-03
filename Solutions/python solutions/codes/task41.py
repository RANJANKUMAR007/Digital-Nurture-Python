import json
class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Department: {self.department}, Salary: {self.salary}"

    def to_dict(self):
        return {"emp_id": self.emp_id, "name": self.name, "department": self.department, "salary": self.salary}

    @classmethod
    def from_dict(cls, data):
        return cls(data["emp_id"], data["name"], data["department"], data["salary"])

def save_employees(employees, filename="emps.json"):
    data = {emp_id: emp.to_dict() for emp_id, emp in employees.items()}
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def load_employees(filename="emps.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            return {emp_id: Employee.from_dict(emp_data) for emp_id, emp_data in data.items()}
    except FileNotFoundError:
        return {}

employees = {
    "101": Employee("101", "Alice", "HR", 50000),
    "102": Employee("102", "Bob", "IT", 60000)
}
save_employees(employees)
loaded_employees = load_employees()
for emp in loaded_employees.values():
    print(emp)
