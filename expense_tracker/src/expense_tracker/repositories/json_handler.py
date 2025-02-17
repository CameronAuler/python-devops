import json
import os

# Define the correct path to the JSON file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Get base directory
FILE_PATH = os.path.join(BASE_DIR, "data", "expenses.json")  # Path to expenses.json

def save_expenses(expenses):
    """Saves a list of expense dictionaries to a JSON file."""
    try:
        os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)  # Ensure 'data' directory exists
        with open(FILE_PATH, "w") as file:
            json.dump(expenses, file, indent=4)  # Write to JSON file with formatting
    except Exception as e:
        print(f"Error saving expenses: {e}")

def load_expenses():
    """Loads expenses from a JSON file, returning a list of dictionaries."""
    if not os.path.exists(FILE_PATH):  # If file doesn't exist, return empty list
        return []

    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)  # Load JSON data
    except json.JSONDecodeError:
        print("Error: The expense file is corrupted. Starting fresh.")
        return []  # Return empty list if JSON is invalid
    except Exception as e:
        print(f"Error loading expenses: {e}")
        return []
