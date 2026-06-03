import csv

def create_dummy_csv():
    with open("employees.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "salary"])
        writer.writerow(["ranjan", "60000"])
        writer.writerow(["kumar", "45000"])
        writer.writerow(["john snow", "80000"])
        writer.writerow(["David", "30000"])

create_dummy_csv()

employees = []
with open("employees.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        employees.append({"name": row["name"], "salary": float(row["salary"])})

high_earners = [emp for emp in employees if emp["salary"] > 50000]
print("Employees with salary > 50000:")
for emp in high_earners:
    print(f"{emp['name']}: {emp['salary']}")

if employees:
    avg_salary = sum(emp["salary"] for emp in employees) / len(employees)
    print(f"Average Salary: {avg_salary:.2f}")
