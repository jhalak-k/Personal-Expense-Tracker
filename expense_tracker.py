from datetime import datetime

FILE_NAME = "expenses.txt"


def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category (Food/Transport/Entertainment/Other): ")
    note = input("Enter note (optional): ")

    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, "a") as file:
        file.write(f"{date},{category},{amount},{note}\n")

    print("Expense added successfully!")


def view_expenses():
    total = 0

    try:
        with open(FILE_NAME, "r") as file:
            print("\nDate\t\tCategory\tAmount\tNote")
            print("-" * 50)

            for line in file:
                date, category, amount, note = line.strip().split(",", 3)

                print(f"{date}\t{category}\t{amount}\t{note}")
                total += float(amount)

        print("-" * 50)
        print("Total:", total)

    except FileNotFoundError:
        print("No expenses found.")


def filter_category():
    target = input("Enter category: ")

    total = 0

    try:
        with open(FILE_NAME, "r") as file:
            print("\nDate\t\tCategory\tAmount\tNote")
            print("-" * 50)

            for line in file:
                date, category, amount, note = line.strip().split(",", 3)

                if category.lower() == target.lower():
                    print(f"{date}\t{category}\t{amount}\t{note}")
                    total += float(amount)

        print("-" * 50)
        print("Subtotal:", total)

    except FileNotFoundError:
        print("No expenses found.")


while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Filter by Category")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        filter_category()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")