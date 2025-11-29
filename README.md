# Expense Tracker 🧾📊

A simple, lightweight, and fully local **command-line Expense Tracker** written in Python.
This project helps you record, update, delete, view, and visualize your daily expenses — all stored in a CSV file. No database, no external dependencies — just pure Python.


---

## 🔥 Features

* ➕ Add expenses
* 🔍 View totals by category
* 🧾 Summary: total + per-category breakdown
* 📈 Charts: pie chart (by category) + bar chart (by month) using `matplotlib`
* ✅ Input validation (amounts, months, categories)
* 💾 Stored in `expense.csv` (simple and portable)

---

## 🚀 Quick start

### Requirements

* Python 3.7+
* `matplotlib`

Install dependencies:

```
python -m pip install -r requirements.txt
```

---

## 🧭 Usage

Run the main script (example assumes `expense_tracker.py`):

### Add an expense

```
python expense_tracker.py add <month> <amount> <category> [note]
# Examples:
python expense_tracker.py add 10 23.5 food Lunch
python expense_tracker.py add March 30 groceries Dinner
```

### View totals for a category (optional month)

```
python expense_tracker.py view <category> [month]
# Example:
python expense_tracker.py view food 10
```

### Summary (total + per-category)

```
python expense_tracker.py summary
```

### Show charts (pie by category + bar by month)

```
python expense_tracker.py chart
```

### Help

```
python expense_tracker.py --help
```

---

## 🗂️ Data format (`expense.csv`)

First row (header) is created automatically on first run:

```
Date added,Month,Amount,Category,Note
2025-11-29,Nov,23.50,food,Lunch
```

* `Date added` — auto-generated (YYYY-MM-DD)
* `Month` — stored as 3-letter month abbrev (e.g., `Jan`, `Feb`, `Mar`)
* `Amount` — numeric (float)
* `Category` — text (case-normalized by the script)
* `Note` — optional text

---

## ⚙️ Tips & Recommendations

* Use numeric months (`10`) or names (`October`) when adding — both are supported.

---

## 🤝 Contributing

Found a bug or have a feature idea? Contributions are welcome!

* Fork the repo, make changes, open a pull request.
* Keep code readable and add tests/examples if possible.

---

## 📝 License

**MIT License** — completely free to use, study, modify, and distribute.


---

## ❤️ Thanks

Thanks for using and improving this small tool
