import csv
from datetime import datetime

def create_dummy_expenses():
    current_date_str = datetime.now().strftime("%Y-%m-%d")
    with open("expenses.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "amount", "category"])
        writer.writerow([current_date_str, "50.0", "Food"])
        writer.writerow([current_date_str, "20.0", "Transport"])
        writer.writerow(["2020-01-01", "100.0", "Food"])
        writer.writerow([current_date_str, "15.0", "Food"])

create_dummy_expenses()

current_year = datetime.now().year
current_month = datetime.now().month

expenses = []
with open("expenses.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            date_val = datetime.strptime(row["date"], "%Y-%m-%d")
            expenses.append({
                "date": date_val,
                "amount": float(row["amount"]),
                "category": row["category"]
            })
        except ValueError:
            continue

current_month_expenses = [
    exp for exp in expenses 
    if exp["date"].year == current_year and exp["date"].month == current_month
]

totals = {}
for exp in current_month_expenses:
    cat = exp["category"]
    totals[cat] = totals.get(cat, 0.0) + exp["amount"]

print(f"Expense Summary for {datetime.now().strftime('%B %Y')}:")
for cat, total in totals.items():
    print(f"{cat}: ${total:.2f}")
