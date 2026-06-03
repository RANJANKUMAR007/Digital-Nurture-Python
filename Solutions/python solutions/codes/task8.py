def find_salary_details(salaries):
    if isinstance(salaries, list) and len(salaries) > 0:
        lowest_salary = min(salaries)
        highest_salary = max(salaries)
        print("Lowest Salary:", lowest_salary)
        print("Highest Salary:", highest_salary)
    else:
        print("Invalid salary list")
salary_list = [50000, 75000, 62000, 95000]
find_salary_details(salary_list)