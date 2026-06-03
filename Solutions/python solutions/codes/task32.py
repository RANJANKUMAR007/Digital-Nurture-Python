def add_expense(expenses, new_expense):
    if not isinstance(new_expense, (int, float)):
        print("Invalid input: Expense must be a number.")
        return
    if new_expense <= 0:
        print("Invalid input: Expense must be greater than 0.")
        return
    expenses.append(new_expense)
    print("Expense added successfully!")
    print("Updated Expenses List:", expenses)
expenses = [100, 250, 75]
add_expense(expenses, 120)