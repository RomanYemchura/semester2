class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.right = None
        self.left = None


class Priority:
    def __init__(self):
        self.heap = []

    def insert(self, value, priority):
        new_node = Node(value, priority)
        self.heap.append(new_node)
        self.heap_sort_up(len(self.heap) - 1)

    def heap_sort_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index].priority > self.heap[parent].priority:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def remove_max(self):
        if not self.heap:
            return None
        max_node = self.heap[0]
        last_node = self.heap.pop()
        if self.heap:
            self.heap[0] = last_node
            self.sort_down(0)
        return max_node.value, max_node.priority

    def sort_down(self, index):
        size = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            biggest = index
            if left < size and self.heap[left].priority > self.heap[biggest].priority:
                biggest = left
            if right < size and self.heap[right].priority > self.heap[index].priority:
                biggest = right
            if biggest != index:
                self.heap[index], self.heap[biggest] = self.heap[biggest], self.heap[index]
                index = biggest
            else:
                break

    def view(self):
        return [(node.value, node.priority) for node in self.heap]


if __name__ == "__main__":
    P = Priority()
    P.insert(5, 7)
    P.insert(1, 9)
    P.insert(2, 2)
    print("Черга до зміни", P.view())
    value, priority = P.remove_max()
    print("Черга після зміни", P.view())
