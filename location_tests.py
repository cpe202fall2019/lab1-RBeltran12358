import unittest
from location import *


class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc), "Location('SLO', 35.3, -120.7)")

    def test_eq_true(self):
        loc1 = Location("Place", 20.1, -20.8)
        loc2 = Location("Place", 20.1, -20.8)
        self.assertTrue(loc1 == loc2)

    def test_eq_false(self):
        loc1 = Location("DifPlace", 30, -20.8)
        loc2 = Location("Place", 20.1, -20.8)
        self.assertFalse(loc1 == loc2)


if __name__ == "__main__":
    unittest.main()
