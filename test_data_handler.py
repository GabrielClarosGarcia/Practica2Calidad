import csv
import pytest
import data_handler


class TestAddExpense:
    def test_add_expense_path1_new_file(self, tmp_path):
        file_name = tmp_path / "expenses.csv"
        data_handler.add_expense("Jan", 20, "food", "lunch", str(file_name))

        with file_name.open(encoding="utf-8", newline="") as file:
            rows = list(csv.reader(file))

        assert rows[0] == ["Date added", "Month", "Amount", "Category", "Note"]
        assert len(rows) == 2
        assert rows[1][1:] == ["Jan", "20.0", "food", "lunch"]

    def test_add_expense_path2_existing_file(self, tmp_path):
        file_name = tmp_path / "expenses.csv"
        file_name.write_text(
            "Date added,Month,Amount,Category,Note\n"
            "2026-10-01,Jan,10.0,food,breakfast\n",
            encoding="utf-8"
        )

        data_handler.add_expense("Feb", 30, "transport", "taxi", str(file_name))
        rows = data_handler.load_csv(str(file_name))

        assert len(rows) == 2
        assert rows[1]["Month"] == "Feb"
        assert rows[1]["Amount"] == "30.0"
        assert rows[1]["Category"] == "transport"
        assert file_name.read_text(encoding="utf-8").count("Date added") == 1

    def test_add_expense_path3_without_note(self, tmp_path):
        file_name = tmp_path / "expenses.csv"
        data_handler.add_expense("Mar", 12, "food", file_name=str(file_name))
        assert data_handler.load_csv(str(file_name))[0]["Note"] == ""

    @pytest.mark.parametrize("amount, expected", [
        ("12.75", "12.75"),
        ("0", "0.0"),
        ("-5", "-5.0"),
    ])
    def test_add_expense_path4_amount_conversion(self, tmp_path, amount, expected):
        file_name = tmp_path / "expenses.csv"
        data_handler.add_expense("Apr", amount, "food", file_name=str(file_name))
        assert data_handler.load_csv(str(file_name))[0]["Amount"] == expected

    def test_add_expense_path5_csv_special_characters(self, tmp_path):
        file_name = tmp_path / "expenses.csv"
        data_handler.add_expense("May", 5, "food", 'bread, "cheese"', str(file_name))
        assert data_handler.load_csv(str(file_name))[0]["Note"] == 'bread, "cheese"'


class TestLoadCSV:
    def test_load_csv_path1_with_data(self, tmp_path):
        file_name = tmp_path / "expenses.csv"
        file_name.write_text(
            "Date added,Month,Amount,Category,Note\n"
            "2026-10-01,Jan,10.0,food,lunch\n"
            "2026-10-02,Feb,30.0,books,book\n",
            encoding="utf-8"
        )

        rows = data_handler.load_csv(str(file_name))
        assert len(rows) == 2
        assert rows[0]["Category"] == "food"
        assert rows[1]["Amount"] == "30.0"

    def test_load_csv_path2_empty_data(self, tmp_path):
        file_name = tmp_path / "expenses.csv"
        file_name.write_text("Date added,Month,Amount,Category,Note\n", encoding="utf-8")
        assert data_handler.load_csv(str(file_name)) == []

    def test_load_csv_path3_missing_file(self, tmp_path):
        with pytest.raises(FileNotFoundError):
            data_handler.load_csv(str(tmp_path / "missing.csv"))