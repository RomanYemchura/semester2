import unittest
from sem2_lab1_2 import pumpkin



class TestPumpkin(unittest.TestCase):
    def test_1(self):
        matrix = [
            [1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]
        ]
        expected_result = [1,2,3,4,8,7,6,5,9,10,11,12,16,15,14,13]
        self.assertEqual(pumpkin(4, 4 ,matrix), expected_result)
    def test_2(self):
        matrix =[
            [1,2,3,4],
            [5,6,7,8],
        ]
        expected_result = [1,2,3,4,8,7,6,5]
        self.assertEqual(pumpkin(2, 4 ,matrix), expected_result)
    def test_3(self):
        matrix =[
            [1],
            [2],
            [3],
            [4],
            [5],
            [6]
        ]
        expected_result = [1,2,3,4,5,6]
        self.assertEqual(pumpkin(6,1,matrix),expected_result)

if __name__ == '__main__':
    unittest.main()
