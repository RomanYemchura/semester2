import unittest
from io import StringIO
from min_depht import bfs


class TestSimpleBFS(unittest.TestCase):

    def test_bfs_chain(self):
        graph = {
            1: [2],
            2: [3],
            3: []
        }
        self.assertEqual(bfs(graph, 1), 3)

    def test_bfs_branching(self):
        graph = {
            1: [2, 3],
            2: [],
            3: [4],
            4: []
        }
        self.assertEqual(bfs(graph, 1), 2)


if __name__ == "__main__":
    unittest.main()
