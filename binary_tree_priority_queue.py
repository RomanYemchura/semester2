class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None


class Priority:
    def __init__(self):
        self.root = None

    def insert_element(self, current_node, new_node):
        if new_node.priority >= current_node.priority:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self.insert_element(current_node.left, new_node)
        else:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self.insert_element(current_node.right, new_node)

    def insert(self, value, priority):
        new_node = Node(value, priority)
        if self.root is None:
            self.root = new_node
        else:
            self.insert_element(self.root, new_node)

    def remove_max(self):
        if self.root is None:
            return None
        parent = None
        current_node = self.root
        while current_node.left:
            parent = current_node
            current_node = current_node.left
        if parent is None:
            self.root = current_node.right
        else:
            parent.left = current_node.right

        return current_node.value, current_node.priority

    def view_queue(self):
        elements = []
        self.inorder(self.root, elements)
        return elements

    def inorder(self, current_node, elements):
        if current_node:
            self.inorder(current_node.left, elements)
            elements.append((current_node.value, current_node.priority))
            self.inorder(current_node.right, elements)


P = Priority()
P.insert(5, 7)
P.insert(1, 9)
P.insert(2, 2)
print(P.view_queue())
removed_value, removed_priority = P.remove_max()
print("Видалено:", removed_value, "з пріоритетом", removed_priority)

