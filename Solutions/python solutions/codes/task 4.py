def calculate_net_salary(salary, tax_rate):
    if salary < 0:
        return "Invalid salary amount"
    if tax_rate < 0 or tax_rate > 1:
        return "Invalid tax rate"
    tax_amount = salary * tax_rate
    net_salary = salary - tax_amount
    return net_salary
salary = 75000.5
tax_rate = 0.18
result = calculate_net_salary(salary, tax_rate)

if isinstance(result, str):
    print(result)
else:
    print(f"Net Salary: {result:.2f}")