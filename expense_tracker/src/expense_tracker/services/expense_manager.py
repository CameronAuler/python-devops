from expense_tracker.models.expense import Expense  # Import Expense class

class ExpenseManager:
    """Manages a list of expenses."""

    def __init__(self):
        """Initialize an empty expense list."""
        self.expenses = []  # List to store expenses

    def add_expense(self, title: str, category: str, date_due: str, cost: float):
        """Creates and adds a new expense to the list."""
        try:
            expense = Expense(title, category, date_due, cost)  # Create expense object
            self.expenses.append(expense)  # Add to list
            print("Expense added successfully!")
        except ValueError as e:
            print(f"Error: {e}")  # Show validation error

    def remove_expense(self, index: int):
        """Removes an expense by index."""
        if 0 <= index < len(self.expenses):  # Validate index
            del self.expenses[index]  # Delete expense from the list
            print("Expense removed successfully!")
        else:
            print("Invalid index. Please enter a valid expense number.")

    def get_expenses(self):
        """Returns the list of expenses (for menu display)."""
        return self.expenses
