import pytest
import utils


class TestIsNumber:
    @pytest.mark.parametrize("value", [
        "123",
        "45.67",
        "-10",
        "-3.14",
        100,
        -5,
        3.1416,
    ])
    def test_is_number_path1_valid_numbers(self, value):
        assert utils.is_number(value) is True

    @pytest.mark.parametrize("value", [
        "abc",
        "",
        "   ",
        "12a",
        "None",
        "$$$",
    ])
    def test_is_number_path2_invalid_inputs(self, value):
        assert utils.is_number(value) is False


class TestIsValidCategory:
    @pytest.mark.parametrize("cat_num", [
        "120",
        "-50.5",
        "0",
        42,
    ])
    def test_is_valid_category_path1_numeric_input(self, cat_num):
        assert utils.is_valid_category(cat_num) is False

    @pytest.mark.parametrize("month_key", [
        "January",
        "january",
        "FEBRUARY",
        "march",
        "December",
    ])
    def test_is_valid_category_path2_full_month_name(self, month_key):
        assert utils.is_valid_category(month_key) is False

    @pytest.mark.parametrize("month_abbr", [
        "Jan",
        "jan",
        "FEB",
        "mar",
        "Dec",
    ])
    def test_is_valid_category_path3_abbreviated_month(self, month_abbr):
        assert utils.is_valid_category(month_abbr) is False

    @pytest.mark.parametrize("valid_cat", [
        "Food",
        "entertainment",
        "Health",
        "Groceries",
        "Utilities",
    ])
    def test_is_valid_category_path4_valid_category(self, valid_cat):
        assert utils.is_valid_category(valid_cat) is True


class TestFindMonth:
    @pytest.mark.parametrize("month_name, expected_abbr", [
        ("January", "Jan"),
        ("january", "Jan"),
        ("MARCH", "Mar"),
        ("december", "Dec"),
        ("July", "Jul"),
    ])
    def test_find_month_path1_valid_month_name(self, month_name, expected_abbr):
        assert utils.find_month(month_name) == expected_abbr

    @pytest.mark.parametrize("invalid_name", [
        "Jan",
        "NotAMonth",
        "invierno",
        "FooBar",
    ])
    def test_find_month_path2_invalid_name_is_num_false(self, invalid_name):
        assert utils.find_month(invalid_name, is_num=False) is None

    @pytest.mark.parametrize("month_num, expected_abbr", [
        (1, "Jan"),
        (2, "Feb"),
        ("5", "May"),
        (10, "Oct"),
        (12, "Dec"),
    ])
    def test_find_month_path3_valid_month_number_is_num_true(self, month_num, expected_abbr):
        assert utils.find_month(month_num, is_num=True) == expected_abbr

    @pytest.mark.parametrize("invalid_num", [
        0,
        13,
        -1,
        100,
        "15",
    ])
    def test_find_month_path4_invalid_month_number_is_num_true(self, invalid_num):
        assert utils.find_month(invalid_num, is_num=True) is None


class TestSortMonthsWithData:
    def test_sort_months_path1_empty_dict(self):
        months, values = utils.sort_months_with_data({})
        assert months == []
        assert values == []

    def test_sort_months_path2_unsorted_months(self):
        data = {"Dec": 120, "Jan": 10, "May": 50, "Feb": 20}
        months, values = utils.sort_months_with_data(data)
        assert months == ["Jan", "Feb", "May", "Dec"]
        assert values == [10, 20, 50, 120]

    def test_sort_months_path3_subset_with_non_month_keys(self):
        data = {"Mar": 30, "Unknown": 999, "Aug": 80}
        months, values = utils.sort_months_with_data(data)
        assert months == ["Mar", "Aug"]
        assert values == [30, 80]

    def test_sort_months_path4_all_twelve_months(self):
        data = {
            "Dec": 12, "Nov": 11, "Oct": 10, "Sep": 9,
            "Aug": 8, "Jul": 7, "Jun": 6, "May": 5,
            "Apr": 4, "Mar": 3, "Feb": 2, "Jan": 1
        }
        months, values = utils.sort_months_with_data(data)
        expected_months = [
            'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
            'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
        ]
        expected_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        assert months == expected_months
        assert values == expected_values
