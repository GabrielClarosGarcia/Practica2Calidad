"""This script has helper functions; formatting, validation"""


def is_number(num):
    """Checks if the input is a number."""
    try:
        float(num)
        return True
    except ValueError:
        return False



def is_valid_category(cat: str):
    """Checks that the category name to not be a month name or number"""

    month_name = {
        'January': 'Jan', 'February': 'Feb', 'March': 'Mar',
        'April': 'Apr', 'May': 'May', 'June': 'Jun',
        'July': 'Jul', 'August': 'Aug', 'September': 'Sep',
        'October': 'Oct', 'November': 'Nov', 'December': 'Dec'
    }

    if is_number(cat):
        return False

    elif (cat.capitalize() in month_name.keys()) or (cat.capitalize() in month_name.values()):
        return False

    else:
        return True



def find_month(month, is_num = False):
    """Find the month abbreviation name by month number or full month name"""
    month_name = {
        'January': 'Jan', 'February': 'Feb', 'March': 'Mar',
        'April': 'Apr', 'May': 'May', 'June': 'Jun',
        'July': 'Jul', 'August': 'Aug', 'September': 'Sep',
        'October': 'Oct', 'November': 'Nov', 'December': 'Dec'
    }
    month_number = {
        1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
        7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
    }

    if str(month).capitalize() in month_name.keys():
        return month_name[str(month).capitalize()]

    elif (is_num == True) and (int(month) in month_number.keys()):
        return month_number[int(month)]

    else:
        print("Not a valid month!")
        return None



def sort_months_with_data(months_data: dict):
    """Sort the input months and values in two seprate lists"""
    month_order = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ]
    sorted_months = [mnth for mnth in month_order if mnth in months_data]
    sorted_values = [months_data[m] for m in sorted_months]
    return sorted_months, sorted_values
