import unittest
from lab1 import *


# A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter_empty(self):
        """ Checks if the functions can identify the max value if it's empty"""
        self.assertEqual(max_list_iter([]), None)

    def test_max_list_iter_beginning_single(self):
        """This test checks if the first value of the list is returned if the list
        is only one value long, since that would be the max"""
        list = [10]
        self.assertEqual(max_list_iter(list), 10)

    def test_max_list_iter_beginning_multiple(self):
        """Checks if the functions can identify the max value if it's in the beginning
        of the list with multiple values in said list"""
        list = [10, 1]
        self.assertEqual(max_list_iter(list), 10)

    def test_max_list_iter_end_multiple(self):
        """Checks if the functions can identify the max value if it's in the end of the
        list"""
        list = [1, 10]
        self.assertEqual(max_list_iter(list), 10)

    def test_max_list_iter_middle_multiple(self):
        """ Checks if the functions can identify the max value if it's in the middle of
        the list"""
        list = [1, 10, 2]
        self.assertEqual(max_list_iter(list), 10)

    def test_max_list_iter_None(self):
        """This test for the exception where the list is None and Raises a ValueError as a
          result of it"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_reverse_rec_ascending_order(self):
        """This test for when the list has multiple positive integers in ascending order"""
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])

    def test_reverse_rec_descending_order(self):
        """This test for when the list has multiple positive integers in descending order"""
        self.assertEqual(reverse_rec([3, 2, 1]), [1, 2, 3])

    def test_reverse_rec_mixed_positive_numbers(self):
        """This test for when the list has multiple positive integers in mixed order"""
        self.assertEqual(reverse_rec([1, 3, 2]), [2, 3, 1])

    def test_reverse_rec_mixed_negative_and_positive_numbers(self):
        """This test for when the list has multiple negative and positive integers in mixed order"""
        self.assertEqual(reverse_rec([-1, 3, -2, -2, 7]), [7, -2, -2, 3, -1])

    def test_reverse_rec_equal_values(self):
        """This test for when the list has multiple positive integers that are all equal"""
        self.assertEqual(reverse_rec([3, 3, 3]), [3, 3, 3])

    def test_reverse_rec_empty(self):
        """This test for when the list is empty, so it should return an empty list back"""
        self.assertEqual(reverse_rec([]), [])

    def test_reverse_rec_None(self):
        """This test for the exception where the list is None and Raises a ValueError as a
          result of it"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)

    def test_bin_search(self):
        """This test for a simple  9 digit sorted list that includes all its values, since the
        low is 0 and the high is the last index"""
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(4, 0, len(list_val) - 1, list_val), 4)

    def test_bin_search_target_not_present(self):
        """This test for a simple  9 digit sorted list that includes all its values, since the
        low is 0 and the high is the last index. This one, however, doesn't include the target and should
        return None"""
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(11, 0, len(list_val) - 1, list_val), None)

    def test_bin_search_None(self):
        """Checks that if the list is None, the ValueError is raised. I used some
        random values for the other parameters as the test failed otherwise"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(10, 0, 1, tlist)

    def test_bin_search_empty(self):
        """Checks to see if the function results in None when the list is empty, since the
        Target value couldn't be in an empty list"""
        list_val = []
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(4, 0, len(list_val) - 1, list_val), None)

    def test_bin_search_single_item_target_present(self):
        """Checks to see if the function can handle having only one item in the list, where it
         should return index 0 if the target is that single value in the list"""
        list_val = [10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(10, 0, len(list_val) - 1, list_val), 0)

    def test_bin_search_single_item_target_not_present(self):
        """Checks to see if the function can handle having only one item in the list, where it
         should return None if the target value and the single number in the list aren't the same."""
        list_val = [18]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(2, 0, len(list_val) - 1, list_val), None)


if __name__ == "__main__":
    unittest.main()
