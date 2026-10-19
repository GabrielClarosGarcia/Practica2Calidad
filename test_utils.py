import utils


class TestIsNumber:
    def test_is_number_path1_valid_number(self):
        assert utils.is_number("123") is True

    def test_is_number_path2_invalid_input(self):
        assert utils.is_number("abc") is False


class TestIsValidCategory:
    def test_is_valid_category_path1_numeric_input(self):
        assert utils.is_valid_category("120") is False

    def test_is_valid_category_path2_full_month_name(self):
        assert utils.is_valid_category("January") is False

    def test_is_valid_category_path3_abbreviated_month(self):
        assert utils.is_valid_category("Jan") is False

    def test_is_valid_category_path4_valid_category(self):
        assert utils.is_valid_category("Food") is True


class TestFindMonth:
    def test_find_month_path1_valid_month_name(self):
        assert utils.find_month("January") == "Jan"

    def test_find_month_path2_invalid_name_is_num_false(self):
        assert utils.find_month("NotAMonth", is_num=False) is None

    def test_find_month_path3_valid_month_number_is_num_true(self):
        assert utils.find_month(10, is_num=True) == "Oct"

    def test_find_month_path4_invalid_month_number_is_num_true(self):
        assert utils.find_month(13, is_num=True) is None


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
