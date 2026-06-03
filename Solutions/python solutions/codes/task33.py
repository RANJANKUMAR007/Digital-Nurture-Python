def merge_employee_data(emp_main, emp_new):
    # Validate inputs
    if not isinstance(emp_main, dict) or not isinstance(emp_new, dict):
        print("Invalid input: Both inputs must be dictionaries.")
        return

    # Update dictionary using .update()
    emp_main.update(emp_new)

    print("Employee data updated successfully!")
    print("Updated Employee Data:", emp_main)


# Existing employee data
employee = {
    "id": 101,
    "name": "Ravi",
    "department": "IT",
    "salary": 45000
}

# New data to merge
new_data = {
    "salary": 50000,
    "city": "Chennai"
}

# Function call
merge_employee_data(employee, new_data)