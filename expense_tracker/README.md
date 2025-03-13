# Expense Tracker Project
The **Expense Tracker** project is designed as a comprehensive learning tool for developers to master fundamental Python concepts through practical application. It covers **basic to advanced Python topics**, starting with variables, data types, and control flow (loops, conditionals) while building an interactive **command-line interface (CLI)** using `input()` and `print()`. Developers will work with **data structures** like lists, dictionaries, and tuples to store and manage expenses efficiently. The project introduces **functions and modular programming**, emphasizing reusable code and separation of concerns. 

Additionally, it explores **file handling** with JSON for data persistence, ensuring users learn to read and write files using `open()`. **Error handling and exceptions** are implemented to manage user input validation and prevent runtime crashes. The project further dives into **object-oriented programming (OOP)** by organizing expense management logic into classes, demonstrating encapsulation, inheritance, and polymorphism. 

To enhance functionality, developers will integrate **date and time operations** using `datetime`, perform **mathematical computations** for expense analysis, and optionally visualize data with `matplotlib`. The project follows industry best practices like **logging, unit testing (unittest), and package structuring** using `setuptools`, reinforcing real-world software development skills. By completing this project, developers will gain a **solid foundation in Python**, improving their ability to build scalable and maintainable applications. 🚀

# 1. Project & Environment Configuration
### 1. Install Python: https://www.python.org/downloads/
### 2. Make a root directory `expense_tracker`.
### 3. Using the terminal, ensure you are in the root directory `cd expense_tracker`.
### 4. Create a virtual environment:
   - Windows:
      - `python -m venv my-env`
      - If you have multiple versions of Python on your system use the `py -0` command to find the latest version of Python on your system and `py -3.<xx> -m venv my-env` to create the virtual environment. Replace `<xx>` wit hthe latest version of Python.
   - Mac/Linux:
      - `python3 -m venv my-env`

### 5. If you are using VSCode then you may have to select the interpreter in the bottom right of the window if it is not auto selected on creation then actiate the venv. If you are creating this project strictly through the terminal, then you only need to activate the vertual environment with the commands...
   - Windows: `.\my-env\Scripts\activate`
   - Mac/Linux: `source my-env/bin/activate`
### 6. Install `setuptools` and `wheel` using the command `pip install setuptools wheel`.
### 7. Add a source directory `src` for your application code.
### 8. Add a package directory within the `src` directory: `/src/expense_tracker`.
### 9. Within `/src/expense_tracker` add a `__init__.py` file which will remain empty to initialize the package and the `main.py` file.

`mian.py` code:
```
def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()
```

### 10. Navigate back to the root directory and create the `pyproject.toml` file and the `setup.py` file.

`pyproject.toml` code:

```
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"
```

`setup.py` code:
```
from setuptools import setup, find_packages

setup(
    name="expense_tracker",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    entry_points={
        'console_scripts': [
            'run=expense_tracker.main:main',
        ],
    },
)
```

### 11. Ensure you are in the root directroy and run the command `pip install -e .` to install the package in editable mode.
### 12. Test the project by using the entry-point command `run` which you set up in the `setup.py` file. Your output should be `Hello, World!`.
### 13. Setup the rest of the project file structure as follows...
```
expense_tracker/
├── src/
│   ├── expense_tracker/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── expense_manager.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── expense.py
│   │   ├── repositories/
│   │   │   ├── __init__.py
│   │   │   ├── json_handler.py
│   │   ├── cli/
│   │   │   ├── __init__.py
│   │   │   ├── menu.py
```

### 14. To manage dependencies...

```
pip freeze > requirements.txt
```

Output (`requirements.txt`):
```
setuptools==75.8.0
...
```

To install or upgrade dependencies from here on out...
```
pip install -r requirements.txt
```

To upgrade dependencies from here on out...
```
pip install --upgrade -r requirements.txt
pip freeze > requirements.txt  # Save new versions
```

# 2. Building the CLI (`src/expense_tracker/cli/menu.py`)
### Import Modules
- Import built-in modules: `sys`, `os`, `time`, and `datetime`.
- Import `ExpenseManager` from `expense_tracker.services.expense_manager`.

### Global Variables
- Create a global instance of `ExpenseManager` to manage expense operations.
- Define a global `DIVIDER_LENGTH` for consistent CLI formatting.
- Define `DIVIDER` using the `DIVIDER_LENGTH` to separate sections in the CLI.

---
### 1. `clear_screen()`
- **Purpose**: Clears the terminal screen for a fresh UI update.
- **Requirements**:
  - Print an ANSI escape sequence (`"\033c"`) to reset the screen.
  - Use `os.system('cls')` for Windows and `os.system('clear')` for macOS/Linux.

### 2. `get_user_choice()`
- **Purpose**: Collects and validates user input for menu navigation.
- **Requirements**:
  - Define a dictionary mapping numeric choices (`"1"`, `"2"`, etc.) and command names (`"add"`, `"rem"`, etc.) to respective actions.
  - Use a `while True` loop to continuously prompt for input until a valid choice is entered.
  - Convert input to lowercase and strip whitespace.
  - Return the corresponding integer value if the input is valid.
  - Print an error message and re-prompt if input is invalid.

### 3. `validate_date(date_str)`
- **Purpose**: Ensures user-entered dates are in the correct format and are not in the past.
- **Requirements**:
  - Accepts a date string in `MM/DD/YYYY` or `MM/DD/YY` format.
  - Use `datetime.strptime()` to parse the date.
  - If parsing fails, prompt the user for re-entry.
  - Ensure the date is today or in the future; otherwise, re-prompt.
  - Return the formatted date in `MM/DD/YYYY` format.

### 4. `validate_cost(cost_str)`
- **Purpose**: Ensures the entered cost is a valid float with two decimal places.
- **Requirements**:
  - Convert the input to `float`, round it to two decimal places.
  - If conversion fails, prompt the user to enter a valid number.
  - Return the validated cost.

### 5. `add_expense_prompt()`
- **Purpose**: Prompts the user to enter a new expense and validates all fields.
- **Requirements**:
  - Collect input for `title`, `category`, `due date`, and `cost`.
  - Validate date using `validate_date()`.
  - Validate cost using `validate_cost()`.
  - Ensure inputs are not empty.
  - Call `expense_manager.add_expense()` with validated data.

### 6. `remove_expense_prompt()`
- **Purpose**: Allows the user to remove an expense by selecting a number.
- **Requirements**:
  - Retrieve current expenses using `expense_manager.get_expenses()`.
  - If no expenses exist, print a message and exit the function.
  - Prompt the user for the expense number to remove.
  - Convert input to an integer and remove the corresponding expense.
  - Handle invalid input gracefully.

### 7. `edit_expense_prompt()`
- **Purpose**: Allows the user to edit an existing expense.
- **Requirements**:
  - Retrieve current expenses using `expense_manager.get_expenses()`.
  - If no expenses exist, print a message and exit the function.
  - Prompt the user to enter the expense number to edit.
  - Allow updating `title`, `category`, `due date`, and `cost`, keeping previous values if left blank.
  - Convert and validate `cost` if entered.
  - Call `expense_manager.edit_expense()` with updated data.

### 8. `pay_expense_prompt()`
- **Purpose**: Marks an expense as paid.
- **Requirements**:
  - Retrieve current expenses using `expense_manager.get_expenses()`.
  - If no expenses exist, print a message and exit the function.
  - Prompt the user for the expense number to mark as paid.
  - Call `expense_manager.pay_expense()` for the selected expense.
  - Handle invalid input gracefully.

### 9. `filter_expenses_prompt()`
- **Purpose**: Allows the user to filter expenses based on a keyword or category.
- **Requirements**:
  - Prompt the user for a search term.
  - Call `expense_manager.filter_expenses()` with the search term.
  - Display filtered expenses in a formatted table.
  - Calculate and display total and remaining (unpaid) costs.
  - Wait for user input before returning to the main menu.

### 10. `display_header()`
- **Purpose**: Displays the CLI header and menu options.
- **Requirements**:
  - Print a formatted title using `DIVIDER_LENGTH`.
  - Display menu options with corresponding numbers and command names.

### 11. `display_expenses()`
- **Purpose**: Displays all recorded expenses in a structured format.
- **Requirements**:
  - Retrieve current expenses using `expense_manager.get_expenses()`.
  - Print a formatted table header.
  - If no expenses exist, display a message.
  - Iterate over expenses and print details, including status (`Paid` or `Unpaid`).
  - Retrieve total and unpaid expenses using `expense_manager.calculate_totals()` and display them.

### 12. `menu()`
- **Purpose**: Main interactive loop for CLI-based expense tracking.
- **Requirements**:
  - Run an infinite loop to display the menu.
  - Call `clear_screen()`, `display_header()`, and `display_expenses()`.
  - Get user input using `get_user_choice()`.
  - Call the corresponding function based on the user’s choice.
  - Handle graceful exit using `sys.exit()` when the user chooses to exit or presses `Ctrl+C`.

# 3. Adding the Expense Class (`src/expense_tracker/models/expense.py`)
### Import Modules
- Import `datetime` from the built-in `datetime` module to handle date validation and formatting.

---

### 1. `class Expense`
- **Purpose**: Represents an individual expense item with attributes for tracking details and payment status.
- **Requirements**:
  - Define an `Expense` class.
  - Store expense details including `title`, `category`, `date_due`, `cost`, and `paid` status.
  - Ensure `cost` is always a float rounded to two decimal places.
  - Default `paid` status should be `False`.

### 2. `__init__(self, title: str, category: str, date_due: str, cost: float, paid: bool = False)`
- **Purpose**: Initializes an `Expense` object with the necessary attributes.
- **Requirements**:
  - Accepts `title`, `category`, `date_due`, `cost`, and `paid` as parameters.
  - Converts `cost` to a `float` and rounds it to two decimal places.
  - Assigns `paid` a default value of `False`.

### 3. `mark_paid(self)`
- **Purpose**: Marks an expense as paid.
- **Requirements**:
  - Set `self.paid` to `True`.

### 4. `mark_unpaid(self)`
- **Purpose**: Marks an expense as unpaid.
- **Requirements**:
  - Set `self.paid` to `False`.

### 5. `__str__(self)`
- **Purpose**: Provides a formatted string representation of the expense for display purposes.
- **Requirements**:
  - Convert `paid` boolean to `"Paid"` or `"Unpaid"`.
  - Format output to align columns correctly.
  - Include `title`, `category`, `date_due`, `cost`, and `paid` status.

# 4. Adding the ExpenseManager Class (`src/expense_tracker/services/expense_manager.py`)
### Import Modules
- Import `Expense` from `expense_tracker.models.expense` to manage individual expenses.
- Import `save_expenses` and `load_expenses` from `expense_tracker.repositories.json_handler` for data persistence.

---

### 1. `class ExpenseManager`
- **Purpose**: Manages a list of expenses, providing methods to add, remove, edit, and retrieve expenses.
- **Requirements**:
  - Encapsulate the expense list (`self.__expenses`) to prevent direct modification.
  - Load existing expenses from a JSON file upon initialization.

### 2. `__init__(self)`
- **Purpose**: Initializes an empty list for storing expenses and loads saved expenses from file.
- **Requirements**:
  - Define `self.__expenses` as a private list.
  - Call `self.load_from_file()` to load saved expenses.

### 3. `add_expense(self, title: str, category: str, date_due: str, cost: float)`
- **Purpose**: Adds a new expense to the list.
- **Requirements**:
  - Create an `Expense` object with the provided parameters.
  - Append the new expense to `self.__expenses`.
  - Call `self.save_to_file()` to update the stored data.
  - Handle `ValueError` exceptions gracefully.

### 4. `remove_expense(self, index: int)`
- **Purpose**: Removes an expense by its index.
- **Requirements**:
  - Ensure the index is within the valid range.
  - Delete the corresponding expense.
  - Call `self.save_to_file()` to persist changes.
  - Display an error message for an invalid index.

### 5. `edit_expense(self, index: int, title: str = None, category: str = None, date_due: str = None, cost: float = None)`
- **Purpose**: Edits an expense’s details.
- **Requirements**:
  - Ensure the index is valid.
  - Retrieve the expense and update only provided fields.
  - Use a lambda function to convert and round `cost` if updated.
  - Save changes using `self.save_to_file()`.

### 6. `pay_expense(self, index: int)`
- **Purpose**: Marks an expense as paid.
- **Requirements**:
  - Validate the index.
  - Call `mark_paid()` on the specified expense.
  - Save the updated data.

### 7. `filter_expenses(self, search_term: str)`
- **Purpose**: Filters expenses by category or keyword.
- **Requirements**:
  - Return a list of expenses where the `title` or `category` matches the search term.

### 8. `calculate_totals(self)`
- **Purpose**: Computes total expenses and remaining unpaid expenses.
- **Requirements**:
  - Use lambda functions to sum total and unpaid costs.
  - Return the total and remaining amounts.

### 9. `get_expenses(self)`
- **Purpose**: Returns the encapsulated expense list.
- **Requirements**:
  - Provide a read-only view of `self.__expenses`.

### 10. `save_to_file(self)`
- **Purpose**: Saves all expenses to a JSON file.
- **Requirements**:
  - Convert `Expense` objects into dictionaries.
  - Call `save_expenses()` to write the data.

### 11. `load_from_file(self)`
- **Purpose**: Loads saved expenses from a JSON file.
- **Requirements**:
  - Retrieve data using `load_expenses()`.
  - Convert dictionary data into `Expense` objects.

### 12. `__str__(self)`
- **Purpose**: Returns a summary of stored expenses.
- **Requirements**:
  - Return a string indicating the number of expenses.

### 13. `__repr__(self)`
- **Purpose**: Returns a formal string representation of `ExpenseManager`.
- **Requirements**:
  - Include the current expense list in the representation.

### 14. `__add__(self, other)`
- **Purpose**: Allows combining two `ExpenseManager` instances.
- **Requirements**:
  - Ensure `other` is an instance of `ExpenseManager`.
  - Merge `self.__expenses` with `other.__expenses`.
  - Return a new `ExpenseManager` instance.

### 15. `__sub__(self, other)`
- **Purpose**: Allows subtracting expenses from another `ExpenseManager`.
- **Requirements**:
  - Ensure `other` is an instance of `ExpenseManager`.
  - Remove matching expenses from `self.__expenses`.
  - Return a new `ExpenseManager` instance.

# 5. Saving to a JSON file (`src/expense_tracker/repositories/json_handler.py`)
### Import Modules
- Import `json` for reading and writing JSON files.
- Import `os` for handling file paths and directory creation.

### Define File Path
- **Purpose**: Establish a consistent location for storing expense data.
- **Requirements**:
  - Determine the base directory using `os.path.abspath(__file__)` and `os.path.dirname()`.
  - Set `FILE_PATH` to `"data/expenses.json"` within the project directory.
  - Ensure the `data` directory exists before writing to the file.

---

### 1. `save_expenses(expenses)`
- **Purpose**: Saves a list of expense dictionaries to a JSON file.
- **Requirements**:
  - Ensure the `data` directory exists using `os.makedirs()`.
  - Open `FILE_PATH` in write mode (`"w"`) and write `expenses` as JSON.
  - Use `json.dump()` with `indent=4` for readable formatting.
  - Handle any exceptions and print an error message if saving fails.

### 2. `load_expenses()`
- **Purpose**: Loads expenses from a JSON file and returns them as a list of dictionaries.
- **Requirements**:
  - Check if `FILE_PATH` exists; return an empty list if not.
  - Open `FILE_PATH` in read mode (`"r"`) and parse JSON data.
  - Handle `json.JSONDecodeError` if the file is corrupted and return an empty list.
  - Handle general exceptions and print an error message if loading fails.
