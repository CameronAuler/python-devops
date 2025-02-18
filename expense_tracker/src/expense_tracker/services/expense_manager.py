from expense_tracker.models.expense import Expense  # Import Expense class
from expense_tracker.repositories.json_handler import save_expenses, load_expenses  # Import JSON functions

class ExpenseManager:
    """Manages a list of expenses with OOP principles applied."""

    def __init__(self):
        """Initialize an encapsulated expense list and load from file."""
        self.__expenses = []  # Encapsulated list of expenses
        self.load_from_file()  # Load existing expenses

    def add_expense(self, title: str, category: str, date_due: str, cost: float):
        """Creates and adds a new expense to the tracker."""
        try:
            expense = Expense(title, category, date_due, cost)
            self.__expenses.append(expense)
            self.save_to_file()
            print("Expense added successfully!")
        except ValueError as e:
            print(f"Error: {e}")

    def remove_expense(self, index: int):
        """Removes an expense by index."""
        if 0 <= index < len(self.__expenses):
            del self.__expenses[index]
            self.save_to_file()
            print("Expense removed successfully!")
        else:
            print("Invalid index. Please enter a valid expense number.")

    def edit_expense(self, index: int, title: str = None, category: str = None, date_due: str = None, cost: float = None):
        """Edits an expense by index, allowing modifications of specific fields."""
        if 0 <= index < len(self.__expenses):
            expense = self.__expenses[index]

            if title:
                expense.title = title
            if category:
                expense.category = category
            if date_due:
                expense.date_due = date_due
            if cost:
                expense.cost = (lambda x: round(float(x), 2))(cost)  # ✅ Lambda for rounding cost

            self.save_to_file()
            print("Expense updated successfully!")
        else:
            print("Invalid index. Please enter a valid expense number.")

    def pay_expense(self, index: int):
        """Marks an expense as paid."""
        if 0 <= index < len(self.__expenses):
            self.__expenses[index].mark_paid()
            self.save_to_file()
            print("Expense marked as paid!")
        else:
            print("Invalid index. Please enter a valid expense number.")

    def filter_expenses(self, search_term: str):
        """Filters expenses based on a search term (category or keyword)."""
        return [
            expense for expense in self.__expenses
            if search_term in expense.category.lower() or search_term in expense.title.lower()
        ]

    def calculate_totals(self):
        """Calculates total and unpaid expenses using lambda."""
        total_cost = (lambda expenses: sum(expense.cost for expense in expenses))(self.__expenses)  
        remaining_cost = (lambda expenses: sum(expense.cost for expense in expenses if not expense.paid))(self.__expenses)  
        return total_cost, remaining_cost

    def get_expenses(self):
        """Getter method to safely access expenses."""
        return self.__expenses

    def save_to_file(self):
        """Converts expenses to dictionaries and saves them using json_handler.py."""
        expense_dicts = [vars(expense) for expense in self.__expenses]
        save_expenses(expense_dicts)

    def load_from_file(self):
        """Loads expenses from file and recreates Expense objects."""
        expense_data = load_expenses()
        self.__expenses = [Expense(**data) for data in expense_data]

    def __str__(self):
        """String representation of ExpenseManager."""
        return f"ExpenseManager with {len(self.__expenses)} expenses"

    def __repr__(self):
        """Official string representation of ExpenseManager."""
        return f"ExpenseManager(expenses={self.__expenses})"

    def __add__(self, other):
        """Operator overloading to combine expenses from two managers."""
        if isinstance(other, ExpenseManager):
            new_manager = ExpenseManager()
            new_manager.__expenses = self.__expenses + other.get_expenses()
            return new_manager
        raise TypeError("Can only add another ExpenseManager.")

    def __sub__(self, other):
        """Operator overloading to subtract expenses from another manager."""
        if isinstance(other, ExpenseManager):
            new_manager = ExpenseManager()
            new_manager.__expenses = [expense for expense in self.__expenses if expense not in other.get_expenses()]
            return new_manager
        raise TypeError("Can only subtract another ExpenseManager.")
