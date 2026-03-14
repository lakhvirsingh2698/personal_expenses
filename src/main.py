from src.models.expense import Expense
from src.services.expense_services import add_expense, view_expenses, update_expense, delete_expense


def get_valid_title():
    while True:
        title = input("Enter title: ").strip()
        if title:
            return title
        print("Title cannot be empty. Please try again.")


def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter amount: ").strip())
            if amount > 0:
                return amount
            print("Amount must be greater than 0.")
        except ValueError:
            print("Invalid amount. Please enter a valid number.")


def get_valid_category():
    while True:
        category = input("Enter category: ").strip()
        if category:
            return category
        print("Category cannot be empty. Please try again.")


def get_valid_date():
    while True:
        expense_date = input("Enter expense date (YYYY-MM-DD): ").strip()

        # Basic format check only for now
        if len(expense_date) == 10 and expense_date[4] == "-" and expense_date[7] == "-":
            return expense_date

        print("Invalid date format. Please use YYYY-MM-DD.")


def get_valid_expense_id(prompt_message):
    while True:
        try:
            expense_id = int(input(prompt_message).strip())
            if expense_id > 0:
                return expense_id
            print("Expense ID must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid numeric ID.")


def handle_add_expense():
    print("\n--- Add Expense ---")
    title = get_valid_title()
    amount = get_valid_amount()
    category = get_valid_category()
    expense_date = get_valid_date()

    expense = Expense(title, amount, category, expense_date)
    add_expense(expense)


def handle_update_expense():
    print("\n--- Update Expense ---")
    expense_id = get_valid_expense_id("Enter expense ID to update: ")
    title = get_valid_title()
    amount = get_valid_amount()
    category = get_valid_category()
    expense_date = get_valid_date()

    expense = Expense(title, amount, category, expense_date)
    update_expense(expense_id, expense)


def handle_delete_expense():
    print("\n--- Delete Expense ---")
    expense_id = get_valid_expense_id("Enter expense ID to delete: ")
    delete_expense(expense_id)


def show_menu():
    print("\n==== Personal Expense Tracker ====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Exit")


def main():
    print("Starting Personal Expense Tracker...")

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            handle_add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            handle_update_expense()

        elif choice == "4":
            handle_delete_expense()

        elif choice == "5":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please select between 1 and 5.")


if __name__ == "__main__":
    main()