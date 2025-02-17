from expense_tracker.models.expense import Expense  # Import Expense class
from expense_tracker.repositories.json_handler import save_expenses, load_expenses  # Import JSON functions

class ExpenseManager:
    """Manages a list of expenses."""

    def __init__(self):
        """Initialize an expense list and load from file."""
        self.expenses = []  # Store expense objects
        self.load_from_file()  # Load existing expenses

    def add_expense(self, title: str, category: str, date_due: str, cost: float):
        """Creates and adds a new expense to the list."""
        try:
            expense = Expense(title, category, date_due, cost)  # Create expense object
            self.expenses.append(expense)  # Add to list
            self.save_to_file()  # Save changes
            print("Expense added successfully!")
        except ValueError as e:
            print(f"Error: {e}")  # Show validation error

    def remove_expense(self, index: int):
        """Removes an expense by index."""
        if 0 <= index < len(self.expenses):  # Validate index
            del self.expenses[index]  # Delete expense from the list
            self.save_to_file()  # Save changes
            print("Expense removed successfully!")
        else:
            print("Invalid index. Please enter a valid expense number.")

    def edit_expense(self, index: int, title: str = None, category: str = None, date_due: str = None, cost: float = None):
        """Edits an expense by index, allowing modifications of specific fields."""
        if 0 <= index < len(self.expenses):  # Validate index
            expense = self.expenses[index]  # Get the selected expense

            # Update only fields provided by the user
            if title:
                expense.title = title
            if category:
                expense.category = category
            if date_due:
                expense.date_due = date_due
            if cost:
                expense.cost = round(float(cost), 2)  # Ensure cost is properly formatted

            self.save_to_file()  # Save changes
            print("Expense updated successfully!")
        else:
            print("Invalid index. Please enter a valid expense number.")

    def pay_expense(self, index: int):
        """Marks an expense as paid."""
        if 0 <= index < len(self.expenses):  # Validate index
            self.expenses[index].mark_paid()  # Mark the expense as paid
            self.save_to_file()  # Save changes
            print("Expense marked as paid!")
        else:
            print("Invalid index. Please enter a valid expense number.")

    def get_expenses(self):
        """Returns the list of expenses (for menu display)."""
        return self.expenses

    def save_to_file(self):
        """Converts expenses to dictionaries and saves them using json_handler.py."""
        expense_dicts = [vars(expense) for expense in self.expenses]  # Convert objects to dicts
        save_expenses(expense_dicts)  # Call json_handler.py

    def load_from_file(self):
        """Loads expenses from file and recreates Expense objects."""
        expense_data = load_expenses()  # Get saved data

        # Convert loaded dictionaries back into Expense objects
        self.expenses = [Expense(**data) for data in expense_data]
