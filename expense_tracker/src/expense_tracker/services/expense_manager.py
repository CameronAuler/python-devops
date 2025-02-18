from expense_tracker.models.expense import Expense  # Import Expense class
from expense_tracker.repositories.json_handler import save_expenses, load_expenses  # Import JSON functions

class ExpenseManager:
    """Manages a list of expenses with OOP principles applied."""

    def __init__(self):
        """Initialize an encapsulated expense list and load from file."""
        self.__expenses = []  # Encapsulated list of expenses to prevent direct modification
        self.load_from_file()  # Load existing expenses from JSON file

    def add_expense(self, title: str, category: str, date_due: str, cost: float):
        """Creates and adds a new expense to the tracker."""
        try:
            expense = Expense(title, category, date_due, cost)  # Create an Expense object
            self.__expenses.append(expense)  # Append the expense to the list
            self.save_to_file()  # Save the updated list to the JSON file
            print("Expense added successfully!")  # Display success message
        except ValueError as e:
            print(f"Error: {e}")  # Print error message if invalid data is encountered

    def remove_expense(self, index: int):
        """Removes an expense by index."""
        if 0 <= index < len(self.__expenses):  # Ensure index is within range
            del self.__expenses[index]  # Delete the expense at the specified index
            self.save_to_file()  # Save changes to the JSON file
            print("Expense removed successfully!")  # Display success message
        else:
            print("Invalid index. Please enter a valid expense number.")  # Error message for invalid index

    def edit_expense(self, index: int, title: str = None, category: str = None, date_due: str = None, cost: float = None):
        """Edits an expense by index, allowing modifications of specific fields."""
        if 0 <= index < len(self.__expenses):  # Ensure index is valid
            expense = self.__expenses[index]  # Retrieve the expense object

            if title:
                expense.title = title  # Update title if provided
            if category:
                expense.category = category  # Update category if provided
            if date_due:
                expense.date_due = date_due  # Update due date if provided
            if cost:
                expense.cost = (lambda x: round(float(x), 2))(cost)  # Inline lambda that converts `x` to float and rounds it to 2 decimal places before assigning it to `expense.cost`

            self.save_to_file()  # Save changes to the JSON file
            print("Expense updated successfully!")  # Display success message
        else:
            print("Invalid index. Please enter a valid expense number.")  # Error message for invalid index

    def pay_expense(self, index: int):
        """Marks an expense as paid."""
        if 0 <= index < len(self.__expenses):  # Ensure index is valid
            self.__expenses[index].mark_paid()  # Mark the expense as paid using Expense class method
            self.save_to_file()  # Save changes to the JSON file
            print("Expense marked as paid!")  # Display success message
        else:
            print("Invalid index. Please enter a valid expense number.")  # Error message for invalid index

    def filter_expenses(self, search_term: str):
        """Filters expenses based on a search term (category or keyword)."""
        return [
            expense for expense in self.__expenses  # Iterate through expenses
            if search_term in expense.category.lower() or search_term in expense.title.lower()  # Match category or title with search term
        ]

    def calculate_totals(self):
        """Calculates total and unpaid expenses using lambda."""
        total_cost = (lambda expenses: sum(expense.cost for expense in expenses))(self.__expenses)  # Lambda function to sum all expenses
        remaining_cost = (lambda expenses: sum(expense.cost for expense in expenses if not expense.paid))(self.__expenses)  # Lambda function to sum only unpaid expenses
        return total_cost, remaining_cost  # Return the total cost and remaining unpaid amount

    def get_expenses(self):
        """Getter method to safely access expenses."""
        return self.__expenses  # Returns the encapsulated list of expenses

    def save_to_file(self):
        """Converts expenses to dictionaries and saves them using json_handler.py."""
        expense_dicts = [vars(expense) for expense in self.__expenses]  # Convert Expense objects to dictionaries
        save_expenses(expense_dicts)  # Save dictionary list to JSON file

    def load_from_file(self):
        """Loads expenses from file and recreates Expense objects."""
        expense_data = load_expenses()  # Retrieve saved expense data from JSON
        self.__expenses = [Expense(**data) for data in expense_data]  # Convert dictionary data back into Expense objects

    def __str__(self):
        """String representation of ExpenseManager."""
        return f"ExpenseManager with {len(self.__expenses)} expenses"  # Return the number of expenses stored

    def __repr__(self):
        """Official string representation of ExpenseManager."""
        return f"ExpenseManager(expenses={self.__expenses})"  # Return an official string representation of the object

    def __add__(self, other):
        """Operator overloading to combine expenses from two managers."""
        if isinstance(other, ExpenseManager):  # Ensure other object is also an ExpenseManager
            new_manager = ExpenseManager()  # Create a new ExpenseManager instance
            new_manager.__expenses = self.__expenses + other.get_expenses()  # Combine expenses from both managers
            return new_manager  # Return the new combined manager
        raise TypeError("Can only add another ExpenseManager.")  # Raise error if other object is not an ExpenseManager

    def __sub__(self, other):
        """Operator overloading to subtract expenses from another manager."""
        if isinstance(other, ExpenseManager):  # Ensure other object is also an ExpenseManager
            new_manager = ExpenseManager()  # Create a new ExpenseManager instance
            new_manager.__expenses = [expense for expense in self.__expenses if expense not in other.get_expenses()]  # Remove expenses that exist in `other`
            return new_manager  # Return the new manager with subtracted expenses
        raise TypeError("Can only subtract another ExpenseManager.")  # Raise error if other object is not an ExpenseManager
