"""This is a expense tracker."""


import sys
from data_handler import add_expense
from analysis import view_expenses, summary
from utils import is_number, is_valid_category, find_month
from visualization import chart



def cmd_process():
    """Process the second argument as a command and call the related functions."""
    cmd = sys.argv[1]

    if cmd == "add":
        month = sys.argv[2]

        amount = sys.argv[3]
        if is_number(amount) == False:
            print("Not a correct price.")
            sys.exit()

        category = sys.argv[4].lower()
        if is_valid_category(category) == False:
            sys.exit()

        note = sys.argv[5].lower() if len(sys.argv) >= 6 else None

        if len(sys.argv) > 6:
            print("Many arguments!")

        month_abbr = find_month(month, is_num=is_number(month))
        if month_abbr == None:
            sys.exit()

        add_expense(month_abbr, amount, category, note)

    elif cmd == "view":
        category = sys.argv[2].lower()
        if is_valid_category(category) == False:
            sys.exit()

        month = sys.argv[3] if len(sys.argv) > 3 else None
        if month != None:
            month_abbr = find_month(month, is_num=is_number(month))
            if month_abbr == None:
                sys.exit()

        if len(sys.argv) > 4:
            print("Many arguments!")

        view_expenses(category, month_name = month_abbr if month != None else None)


    elif cmd == "summary":
        if len(sys.argv) > 2:
            print("Many arguments!")
        summary()

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


if __name__ == "__main__":
    try:
        cmd_process()
    except IndexError:
        print("⚠️  Missing arguments. Use 'python expense_tracker.py --help' for usage info.")
    except FileNotFoundError:
        print("No data found yet!")
