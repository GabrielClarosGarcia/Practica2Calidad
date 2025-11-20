"""This is a expense tracker."""


import sys
from data_handler import add_expense
from analysis import view_expenses, summary
from utils import is_number, is_valid_category, find_month
from visualization import chart
from config import configure



def cmd_process():
    """Process the second argument as a command and call the related functions."""
    cmd = sys.argv[1]
    settings = configure()

    if cmd == "add":
        month = sys.argv[2]

        amount = sys.argv[3]
        if not is_number(amount):
            raise InvalidPrice("Not a correct price!")

        category = sys.argv[4].lower()
        if not is_valid_category(category):
            raise InvalidCategory("Invalid category name!")

        note = sys.argv[5].lower() if len(sys.argv) >= 6 else None

        if len(sys.argv) > 6:
            print("Many arguments!")

        month_abbr = find_month(month, is_num=is_number(month))
        if month_abbr == None:
            raise InvalidMonthName("Not a valid month!")

        add_expense(month_abbr, amount, category, note, file_name=settings["data_file"])

    elif cmd == "view":
        category = sys.argv[2].lower()
        if not is_valid_category(category):
            raise InvalidCategory("Invalid category name!")

        month = sys.argv[3] if len(sys.argv) > 3 else None
        if month != None:
            month_abbr = find_month(month, is_num=is_number(month))
            if month_abbr == None:
                raise InvalidMonthName("Not a valid month!")

        if len(sys.argv) > 4:
            print("Many arguments!")

        view_expenses(
            category, month_name = month_abbr if month != None else None, fl_name=settings["data_file"], currency=settings["currency"]
            )


    elif cmd == "summary":
        if len(sys.argv) > 2:
            print("Many arguments!")
        summary(fl_name=settings["data_file"], currency=settings["currency"])

    elif cmd == "chart":
        chart()

    elif cmd == "--help":
        msg = """
Usage:
  add <month> <amount> <category> [note]    Add a new expense
  view <category> [month]                   View expenses
  summary                                   Show total spending
  chart                                     Show spending chart

  Examples:
  python expense_tracker.py add 10 23.5 food Lunch
  python expense_tracker.py add March 30 food Dinner
  python expense_tracker.py view food 10
"""
        print(msg)


class Error(Exception):
    """Base class for custom errors."""
    pass

class InvalidPrice(Error):
    """Raises when the price is incorrect."""
    pass

class InvalidCategory(Error):
    """Raises when the category is not correct."""
    pass

class InvalidMonthName(Error):
    """Raises when the month name is not valid."""
    pass


if __name__ == "__main__":
    try:
        cmd_process()
    except IndexError:
        print("⚠️  Missing arguments. Use 'python expense_tracker.py --help' for usage info.")
    except FileNotFoundError:
        print("No data found yet!")
    except Error as error:
        print(error)
