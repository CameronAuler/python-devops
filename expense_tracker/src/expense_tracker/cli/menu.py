import sys
import os
import time
from datetime import datetime
from expense_tracker.services.expense_manager import ExpenseManager

# Create a global ExpenseManager instance
expense_manager = ExpenseManager()

def clear_screen():
    """Clears the terminal screen after a short delay to give an updating effect."""
    time.sleep(2)  # Pause to allow user to read messages before clearing screen
    os.system('cls' if os.name == 'nt' else 'clear')  # Windows -> cls | macOS/Linux -> clear

def get_user_choice():
    """Gets and validates user input, allowing numbers or command names."""
    valid_choices = {"1": 1, "add": 1, 
                     "2": 2, "rem": 2, 
                     "3": 3, "edit": 3, 
                     "4": 4, "pay": 4, 
                     "5": 5, "exit": 5}

    while True:
        choice = input("Enter your choice (1-5 or command name): ").strip().lower()  # Convert input to lowercase
        if choice in valid_choices:
            return valid_choices[choice]  # Return corresponding number for processing
        print("Invalid choice. Please enter a number (1-5) or a valid command name (add, rem, edit, pay, exit).")  # Error message if invalid

def validate_date(date_str):
    """Ensures the date is correctly formatted as MM/DD/YYYY, allowing variations like 7/4/24 and ensuring it's today or later."""
    while True:
        try:
            parsed_date = datetime.strptime(date_str, "%m/%d/%y")  # Try parsing short format (MM/DD/YY)
            formatted_date = parsed_date.strftime("%m/%d/%Y")  # Convert to full format (MM/DD/YYYY)
        except ValueError:
            try:
                parsed_date = datetime.strptime(date_str, "%m/%d/%Y")  # Try parsing full format (MM/DD/YYYY)
                formatted_date = parsed_date.strftime("%m/%d/%Y")  
            except ValueError:
                date_str = input("Invalid date format. Enter date as MM/DD/YYYY: ").strip()  # Prompt again for correct format
                continue

        # Ensure the date is today or in the future
        if parsed_date.date() >= datetime.today().date():
            return formatted_date  # Return valid date

        print("The due date must be today or in the future.")  # Error message for past dates
        date_str = input("Enter a valid future date (MM/DD/YYYY): ").strip()  # Re-prompt user for valid input

def validate_cost(cost_str):
    """Ensures the cost is a valid float and always has two decimal places."""
    while True:
        try:
            cost = round(float(cost_str), 2)  # Convert to float and round to 2 decimal places
            return cost
        except ValueError:
            cost_str = input("Invalid cost. Enter a valid amount (e.g., 100.00): ").strip()  # Re-prompt user for valid input

def add_expense_prompt():
    """Prompts the user to enter expense details and ensures each field is valid before proceeding."""

    while True:
        title = input("Enter expense title: ").strip().title()  # Capitalize first letter of each word
        if title:
            break
        print("Title is required. Please enter a valid title.")  # Error message if input is empty

    while True:
        category = input("Enter expense category: ").strip().title()  # Capitalize first letter of each word
        if category:
            break
        print("Category is required. Please enter a valid category.")  # Error message if input is empty

    while True:
        date_due = input("Enter due date (MM/DD/YYYY): ").strip()  # Prompt for due date
        date_due = validate_date(date_due)  # Validate and format the date
        if date_due:
            break

    while True:
        cost = input("Enter expense cost: ").strip()  # Prompt for cost
        cost = validate_cost(cost)  # Validate and format the cost
        if cost:
            break

    expense_manager.add_expense(title, category, date_due, cost)  # Add validated expense
    print(f"Expense added successfully: {title}, {category}, {date_due}, ${cost:.2f}")  # Confirmation message
    time.sleep(2)  # Pause before clearing screen

def remove_expense_prompt():
    """Prompts the user to remove an expense by its number."""
    expenses = expense_manager.get_expenses()

    if not expenses:
        print("No expenses to remove.")
        time.sleep(2)
        return

    while True:
        try:
            index = int(input("Enter the expense number to remove: ")) - 1  # Convert to zero-based index
            expense_manager.remove_expense(index)  # Remove expense
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def edit_expense_prompt():
    """Prompts the user to edit an expense's details."""
    expenses = expense_manager.get_expenses()

    if not expenses:
        print("No expenses to edit.")
        time.sleep(2)
        return

    while True:
        try:
            index = int(input("Enter the expense number to edit: ")) - 1  # Convert to zero-based index
            if 0 <= index < len(expenses):
                break
            print("Invalid number. Please enter a valid expense number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Prompt for each editable field
    title = input("Enter new title (or press Enter to keep current): ").strip().title() or None
    category = input("Enter new category (or press Enter to keep current): ").strip().title() or None
    date_due = input("Enter new due date (MM/DD/YYYY) or press Enter to keep current: ").strip() or None
    cost = input("Enter new cost (or press Enter to keep current): ").strip() or None

    # Convert cost only if the user entered a value
    cost = round(float(cost), 2) if cost else None

    expense_manager.edit_expense(index, title, category, date_due, cost)

def pay_expense_prompt():
    """Prompts the user to mark an expense as paid."""
    expenses = expense_manager.get_expenses()

    if not expenses:
        print("No expenses to mark as paid.")
        time.sleep(2)
        return

    while True:
        try:
            index = int(input("Enter the expense number to mark as paid: ")) - 1  # Convert to zero-based index
            expense_manager.pay_expense(index)  # Mark expense as paid
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def display_header():
    """Displays the menu header and available commands with correct formatting."""
    print("\n" + "=" * 120)  # Extended width to avoid line breaks
    print(f"{'Expense Tracker'.center(120)}")  # Center title properly
    print("=" * 120)
    print("1. Add Expense (add)  |  2. Remove Expense (rem)  |  3. Edit Expense (edit)  |  4. Pay Expense (pay)  |  5. Exit (exit)")
    print("=" * 120)

def display_expenses():
    """Displays all stored expenses in a formatted way with fixed column widths."""
    print("-" * 120)
    print(f"{'No.':<5} {'Expense':<20} {'Category':<20} {'Due Date':<15} {'Cost':<10} {'Status':<10}")  # Align headers properly
    print("-" * 120)

    expenses = expense_manager.get_expenses()  # Retrieve list of expenses

    if not expenses:  # Check if there are expenses to display
        print("No expenses recorded yet.")  # Show message if list is empty
    else:
        for idx, expense in enumerate(expenses, start=1):  # Loop through each expense
            status_text = "Paid" if expense.paid else "Unpaid"  # Convert boolean to readable text
            print(f"{idx:<5} {expense.title:<20} {expense.category:<20} {expense.date_due:<15} ${expense.cost:<10.2f} {status_text:<10}")  
    print("-" * 120)  # Closing separator


def menu():
    """Runs the interactive CLI menu system."""
    while True:
        clear_screen()
        display_header()
        display_expenses()

        choice = get_user_choice()

        if choice == 1:
            add_expense_prompt()
        elif choice == 2:
            remove_expense_prompt()
        elif choice == 3:
            edit_expense_prompt()
        elif choice == 4:
            pay_expense_prompt()
        elif choice == 5:
            print("Exiting the Expense Tracker. Goodbye!")
            sys.exit()
