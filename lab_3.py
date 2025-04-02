class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def sum_left_leaves(node):
    if not node:
        return 0

    total = 0

    if node.left and not node.left.left and not node.left.right:
        total += node.left.value

    total += sum_left_leaves(node.left)
    total += sum_left_leaves(node.right)

    return total


# Приклад дерева
root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)
root.right.left = BinaryTree(15)
root.right.right = BinaryTree(7)

print(sum_left_leaves(root))