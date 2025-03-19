import unittest
from lab_2_exercise_2 import sum_of_three

class TestSum(unittest.TestCase):
    def test_1(self):
        self.assertTrue(sum_of_three([1,5,7,9,3,4], 21))
    def test_2(self):
        self.assertTrue(sum_of_three([1,2,7,9,8,4], 13))
    def test_3(self):
        self.assertFalse(sum_of_three([1,2,3,4,5,6,7,8,9,10], 199))
