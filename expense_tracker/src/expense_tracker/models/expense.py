from datetime import datetime  # Import datetime for date validation

class Expense:
    """Class to represent an individual expense."""

    def __init__(self, title: str, category: str, date_due: str, cost: float, paid: bool = False):
        """Initialize an expense object with title, category, due date, cost, and paid status."""
        self.title = title  # Store expense title
        self.category = category  # Store expense category
        self.date_due = self.validate_date(date_due)  # Validate and store the due date
        self.cost = round(float(cost), 2)  # Convert cost to float and round to 2 decimal places
        self.paid = paid  # Store expense status as boolean (True = Paid, False = Unpaid)

    @staticmethod
    def validate_date(date_str: str) -> str:
        """Validates and formats date as MM/DD/YYYY."""
        try:
            formatted_date = datetime.strptime(date_str, "%m/%d/%Y").strftime("%m/%d/%Y")  
            return formatted_date  # Return formatted date
        except ValueError:
            raise ValueError("Invalid date format. Use MM/DD/YYYY.")  # Raise an error for invalid date

    def mark_paid(self):
        """Marks the expense as paid."""
        self.paid = True  # Set status to True (Paid)

    def mark_unpaid(self):
        """Marks the expense as unpaid."""
        self.paid = False  # Set status to False (Unpaid)

    def __str__(self):
        """String representation of an expense for display."""
        status = "Paid" if self.paid else "Unpaid"  # Convert boolean to text
        return f"{self.title:<15} {self.category:<15} {self.date_due:<15} ${self.cost:<10.2f} {status}"  # Format display output
