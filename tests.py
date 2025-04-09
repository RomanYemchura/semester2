import unittest
from binary_tree_priority_queue import Priority
class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.P = Priority()

    def test_insert_and_view(self):
        self.P.insert(10, 3)
        self.P.insert(20, 5)
        self.P.insert(30, 1)
        result = self.P.view_queue()
        self.assertEqual(result, [(20, 5), (10, 3), (30, 1)])

    def test_remove_max(self):
        self.P.insert(100, 9)
        self.P.insert(200, 7)
        removed = self.P.remove_max()
        self.assertEqual(removed, (100, 9))
        self.assertEqual(self.P.view_queue(), [(200, 7)])

    def test_remove_from_empty(self):
        self.assertIsNone(self.P.remove_max())

if __name__ == '__main__':
    unittest.main()
