import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

class Category:
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.spent = 0.0

    def add_expense(self, amount):
        self.spent += amount
        if self.spent > self.limit:
            print(f"Alert: {self.name} category has exceeded budget limit of {self.limit} (Spent: {self.spent})")

categories = {
    "Food": Category("Food", 200),
    "Transport": Category("Transport", 100),
    "Entertainment": Category("Entertainment", 150)
}

expenses_input = [
    ("Food", 150),
    ("Transport", 50),
    ("Entertainment", 200),
    ("Food", 60)
]

for cat_name, amount in expenses_input:
    if cat_name in categories:
        categories[cat_name].add_expense(amount)

labels = [cat.name for cat in categories.values()]
sizes = [cat.spent for cat in categories.values()]

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
plt.title("Monthly Expenses by Category")
plt.savefig("budget.png")
print("Budget visualization saved to budget.png")
