"""This is a test file"""


import data_handler
import tempfile


def test_add_expense_empty_file():
    """A temporary file will be used to check the correct functionality of add_expense function
    in a situation that the file is exists but empty.
    """
    with tempfile.NamedTemporaryFile(mode="w+", newline="", delete_on_close=False) as temp_file:
        data_handler.add_expense("Feb", float(300), "utilities", "electricity bill", file_name=temp_file.name)

        temp_file.seek(0)
        lines = temp_file.readlines()

        assert "Date added,Month,Amount,Category,Note" in lines[0], "Title not correct"


def test_add_expense_written_file():
    """This time the file has a header and is not empty."""
    with tempfile.NamedTemporaryFile(mode="w+", newline="", delete_on_close=False) as temp_file:
        temp_file.write("Date added,Month,Amount,Category,Note")
        data_handler.add_expense("May", float(50), "food", "lunch", file_name=temp_file.name)

        temp_file.seek(0)
        lines = temp_file.readlines()

        assert "May,50.0,food,lunch" in lines[1], "Data not correct"


def test_load_csv():
    """load_csv return value will be test."""
    with tempfile.NamedTemporaryFile(mode="w+", newline="", delete_on_close=False) as temp_file:
        temp_file.write(
            "Date added,Month,Amount,Category,Note\n\
            2025-01-10,Jan,75.0,food,lunch\n\
            2025-01-29,Jan,450.0,grocery,weekly groceries\n"
        )

        temp_file.seek(0)
        read_file = data_handler.load_csv(temp_file.name)
        print(read_file)
        assert type(read_file) == list, "Data output is in a invalid form"
