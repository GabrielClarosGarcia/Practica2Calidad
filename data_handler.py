"""This script handles cvs reading & writting tasks"""

import csv
from datetime import datetime



def add_expense(month: str, amount: float, category: str, note = None, file_name = "expense.csv"):
    """Write input data in the csv file."""
    with open(file_name, "a+", encoding="utf-8", newline="") as file:

        file.seek(0)

        if file.read(5) == "":
            writer = csv.writer(file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(["Date added", "Month", "Amount", "Category", "Note"])
        else:
            writer = csv.writer(file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)

        now_date = datetime.now().date()

        writer.writerow([now_date, month, float(amount), category, note])
        print(f"✅ Added expense: {amount} in {category.capitalize()} ({month})")


def load_csv(file_name = "expense.csv"):
    """Read the csv file and return the data as a list of dictionaries."""
    with open(file_name, "r", encoding="utf-8", newline="") as file:
        read_csv = list(csv.DictReader(file))
        return read_csv
