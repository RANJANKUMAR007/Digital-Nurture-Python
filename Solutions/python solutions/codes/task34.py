def get_employee_salary(company, department, employee_name):
    if not isinstance(company, dict):
        print("Invalid input: Company data must be a dictionary.")
        return

    if department not in company:
        print("Error: Department not found.")
        return

    if not isinstance(company[department], dict):
        print("Invalid data format inside department.")
        return

    if employee_name not in company[department]:
        print("Error: Employee not found in the department.")
        return
    salary = company[department][employee_name]
    print(f"{employee_name}'s salary is: {salary}")
company_data = {
    "IT": {
        "Ravi": 50000,
        "Kumar": 45000
    },
    "HR": {
        "Anita": 40000,
        "Meena": 42000
    },
    "Finance": {
        "John": 60000
    }
}

get_employee_salary(company_data, "IT", "Ravi")