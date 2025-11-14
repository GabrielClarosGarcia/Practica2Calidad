"""Test"""


import unittest
import utils


class TestUtils(unittest.TestCase):
    # is_number 
    def test_is_number_valid_str_input(self):
        self.assertTrue(utils.is_number("50000"), "str: int number")
    def test_is_number_valid_str_input_2(self):
        self.assertTrue(utils.is_number("25.40"), "str: float number")
    def test_is_number_valid_int_input(self):
        self.assertTrue(utils.is_number(20000), "int")
    def test_is_number_negetive_int_input(self):
        self.assertTrue(utils.is_number(-20), "int")
    def test_is_number_unvalid_str_input(self):
        self.assertFalse(utils.is_number("String"), "String input")
    def test_is_number_empty_str(self):
        self.assertFalse(utils.is_number(""), "Empty str")

    # is_valid_category 
    def test_is_valid_category_month_input(self):
        self.assertFalse(utils.is_valid_category("March"), "Full month name")
    def test_is_valid_category_full_month_input_lowercase(self):
        self.assertFalse(utils.is_valid_category("May".lower()), "Full month name lowercase")
    def test_is_valid_category_abbr_month_input_lowercase(self):
        self.assertFalse(utils.is_valid_category("Feb".lower()), "Abbr month name lowercase")
    def test_is_valid_category_num_input(self):
        self.assertFalse(utils.is_valid_category(35), "Number")
    def test_is_valid_category_correct_input(self):
        self.assertTrue(utils.is_valid_category("Food"), "Valid category name")

    # find_month 
    def test_find_month_full_month_name(self):
        self.assertEqual(utils.find_month("January"), "Jan", "Full month name")
    def test_find_month_full_month_name_lowercase(self):
        self.assertEqual(utils.find_month("march"), "Mar", "Full month name")
    def test_find_month_by_month_number(self):
        self.assertEqual(utils.find_month(10, is_num=True), "Oct", "Month number")
    def test_find_month_by_wrong_month_name(self):
        self.assertIsNone(utils.find_month("Feb"), "Wrong Month name")
    def test_find_month_by_wrong_month_number(self):
        self.assertIsNone(utils.find_month(14, is_num=True), "Wrong Month number")

    # sort_months_with_data 
    def test_sort_months_with_data(self):
        data = {"Mar": 20, "Jan": 10, "Feb": 15}
        output = (["Jan", "Feb", "Mar"], [10, 15, 20])
        self.assertTupleEqual(utils.sort_months_with_data(data), output)


if __name__ == "__main__":
    unittest.main()
