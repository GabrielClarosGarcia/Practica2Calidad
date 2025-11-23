"""This script do visualization tasks."""


from data_handler import load_csv
from utils import sort_months_with_data
import matplotlib.pyplot as plt



def chart(file_name):
    """Make pie and bar Charts"""
    read_csv = load_csv(file_name=file_name)

    pie_data = {}
    for item in read_csv:
        pie_data[item["Category"]] = pie_data.get(item["Category"], 0) + float(item["Amount"])
    categories = list(pie_data.keys())
    prices = list(pie_data.values())

    bar_data = {}
    for item in read_csv:
        bar_data[item["Month"]] = bar_data.get(item["Month"], 0) + float(item["Amount"])
    bar_month, bar_cost = sort_months_with_data(bar_data)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    ax1.pie(prices, labels=categories, shadow=True, autopct="%1.2f%%")
    ax1.legend(title="Categories:")
    ax1.set_title("Category Costs")
    ax1.axis("equal")

    ax2.bar(bar_month, bar_cost)
    ax2.set_title('Monthly Costs')
    ax2.set_xlabel("Months")
    ax2.set_ylabel("Total Costs")

    plt.tight_layout()

    plt.show()
