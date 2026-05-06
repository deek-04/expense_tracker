from datetime import datetime

expenses = []

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    expense = {
        "amount": amount,
        "category": category,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    expenses.append(expense)

    print("Expense added successfully!")


def view_expenses():
    if len(expenses) == 0:
        print("No expenses found.\n")
    else:
        print("\n--- All Expenses ---")
        for exp in expenses:
            print(f"Amount: {exp['amount']} | Category: {exp['category']} | Time: {exp['time']}")
        print()

def total_expense():
    total = 0
    for exp in expenses:
        total += exp['amount']
    
    print("Total Expense:", total, "\n")

while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_expense()

    elif choice == '2':
        view_expenses()

    elif choice == '3':
        total_expense()

    elif choice == '4':
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.\n")