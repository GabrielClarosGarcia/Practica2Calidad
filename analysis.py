"""This script do analysis tasks"""


from data_handler import load_csv


def view_expenses(category, month_name = None):
    csv_data = load_csv()
    sum_of_prices = 0.0
    for item in csv_data:
        if month_name == None:
            if item["Category"] == category:
                sum_of_prices += float(item["Amount"])
        else:
            if (item["Category"] == category) and (item["Month"] == month_name):
                sum_of_prices += float(item["Amount"])

    print(f"Total amount of money spend on {category.capitalize()}: {sum_of_prices}")



def summary():
    read_csv = load_csv()
    sum_of_prices = 0.0
    for item in read_csv:
        sum_of_prices += float(item["Amount"])
    print(f"Total spent: {sum_of_prices}")

    category_price = {}
    for item in read_csv:
        category_price[item["Category"]] = category_price.get(item["Category"], 0) + float(item["Amount"])
    for category, price in category_price.items():
        print(f"Total spent on {category}: {price}")
