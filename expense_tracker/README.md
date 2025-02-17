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

### 5. If you are using VSCode then you can select the interpreter in the bottom right of the window if it is not auto selected on creation. If you are creating this project strictly through the terminal, then you need to activate the vertual environment with the commands...
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
### 13. To manage dependencies

```
pip freeze > requirements.txt
```
Output:
```
fastapi==0.110.0
uvicorn==0.29.0
openai==1.3.5
redis==5.0.1
pytest==8.0.2
...
```

To install or upgrade dependencies from here on out...
```
pip install -r requirements.txt
```
```
pip install --upgrade -r requirements.txt
pip freeze > requirements.txt  # Save new versions
```

# CLI


# expense_manager