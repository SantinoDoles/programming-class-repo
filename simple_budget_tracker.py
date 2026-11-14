import locale

def get_income():
     while True:
            income = input("Enter your total income: ")
            try:
                income = float(income)
                if income < 0:
                    raise ValueError("Income cannot be negative.")
                return income 
            except ValueError:
                print("Please enter a valid non-negative number.")

def get_expenses():
    expenses = []

    while True:
            expense = input("Enter an expense, or type 'done' to finish: ")
            if expense == "done":
                break
            if expense == "0":
                break 
            try:
                expense = float(expense)
                if expense < 0:
                    raise ValueError("Expense cannot be negative.")
                expenses.append(expense)
            except ValueError:
                print("Please enter a valid expense amount.")
    return expenses 


def main():
    locale.setlocale(locale.LC_ALL, "English_United States.1252")
    print("Welcome to the Simple Budget Tracker!")

    income = get_income()
    expenses = get_expenses()

    total_expenses = sum(expenses)
    remaining_budget = income - total_expenses 

    print(f"Total Income: ${income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Remaining Budget: ${remaining_budget:.2f}")

    print("\nExpense Breakdown:")

    for number, expense in enumerate(expenses, start=1):
        print(f"{number}, {locale.currency(expense, grouping = True)}")

    print("Completed by, Santino Doles")

main()
