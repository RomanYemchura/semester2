import unittest
from lab_3 import BinaryTree, sum_left_leaves

class TestBinaryTree(unittest.TestCase):
    def test_sum_left_leaves(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        root.right.left = BinaryTree(15)
        root.right.right = BinaryTree(7)
        self.assertEqual(sum_left_leaves(root), 24)

    def test_sum_left_leaves_2(self):
        root = BinaryTree(3)
        root.right = BinaryTree(20)
        root.right.right = BinaryTree(7)
        self.assertEqual(sum_left_leaves(root), 0)


