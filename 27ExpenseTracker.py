import 

FILE_NAME = "expenses.txt"

def add_expense():
    date = input("Date (DD-MM-YYYY): ").strip()
    category = input("Category (Food/Travel/Shopping/etc): ").strip()
    amount = float(input("Amount: ").strip())
    note = input("Note: ").strip()

    with open(FILE_NAME, "a") as f:
        f.write(f"{date},{category},{amount},{note}\n")

    print("Expense added")

def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found")
        return

    with open(FILE_NAME, "r") as f:
        lines = f.readlines()

    if not lines:
        print("No expenses found")
        return

    print("\nDate | Category | Amount | Note")
    print("-" * 40)
    for line in lines:
        date, category, amount, note = line.strip().split(",", 3)
        print(f"{date} | {category} | {amount} | {note}")

def total_expense():
    if not os.path.exists(FILE_NAME):
        print("No expenses found")
        return

    total = 0
    with open(FILE_NAME, "r") as f:
        for line in f:
            parts = line.strip().split(",", 3)
            total += float(parts[2])

    print("Total Expense:", total)

def category_total():
    if not os.path.exists(FILE_NAME):
        print("No expenses found")
        return

    totals = {}
    with open(FILE_NAME, "r") as f:
        for line in f:
            date, category, amount, note = line.strip().split(",", 3)
            amount = float(amount)
            totals[category] = totals.get(category, 0) + amount

    print("\nCategory Wise Total:")
    for cat, amt in totals.items():
        print(f"{cat}: {amt}")

def main():
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Category Wise Total")
        print("5. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            category_total()
        elif choice == "5":
            print("Bye")
            break
        else:
            print("Invalid choice")

main()
