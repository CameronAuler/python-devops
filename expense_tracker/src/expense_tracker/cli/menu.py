import sys
from expense_tracker.services.expense_manager import ExpenseManager  # Import ExpenseManager

# Create a global ExpenseManager instance
expense_manager = ExpenseManager()

def display_header():
    print("\n" + "-" * 100)
    print(f"{'Expense Tracker'.center(100)}")
    print("=" * 100)
    print("1. Add Expense   |   2. Remove Expense   |   3. Edit Expense   |   4. Pay Expense   |   5. Exit   ")
    print("=" * 100)



def get_user_choice():
    """Gets and validates user input."""
    try:
        choice = int(input("Enter your choice (1-5): "))  # Get user input
        if choice not in range(1, 6):  # Ensure input is between 1 and 5
            print("Invalid choice. Please enter a number between 1 and 5.")  # Error message
            return None
        return choice  # Return valid choice
    except ValueError:
        print("Invalid input. Please enter a numeric value.")  # Error message
        return None



def add_expense_prompt():
    """Prompts the user to enter expense details and adds the expense."""
    title = input("Enter expense title: ").strip()
    category = input("Enter expense category: ").strip()
    date_due = input("Enter due date (MM/DD/YYYY): ").strip()
    cost = input("Enter expense cost: ").strip()

    if not title or not category or not date_due or not cost:  # Ensure all fields are filled
        print("All fields are required. Please try again.")
        return

    try:
        expense_manager.add_expense(title, category, date_due, float(cost))  # Add expense
    except ValueError:
        print("Invalid cost value. Please enter a valid number.")



def display_expenses():
    """Displays all stored expenses in a formatted way."""
    print("-" * 100)
    print("      Expense    |       Category        |      Due Date       |        Cost        |   Status   ")
    print("-" * 100)

    expenses = expense_manager.get_expenses()  # Get expenses from manager

    if not expenses:  # If no expenses exist
        print("No expenses recorded yet.")  # Show message
    else:
        for idx, expense in enumerate(expenses, start=1):  # Loop through expenses
            print(f"{idx}. {expense}")  # Print formatted expense details
    print("-" * 100)

def menu():
    """Runs the interactive CLI menu system."""
    while True:
        display_header()  # Display menu header
        display_expenses() # Display current expenses
        choice = get_user_choice()  # Get user choice

        if choice == 1:
            add_expense_prompt()  # Add an expense
        elif choice == 2:
            print("remove expense coming soon")
        elif choice == 3:
            print("edit expense coming soon")
        elif choice == 4:
            print("pay expense coming soon")
        elif choice == 5:
            print("Exiting the Expense Tracker. Goodbye!")  # Exit message
            sys.exit()  # Exit program
