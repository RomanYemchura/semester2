from collections import deque


def read_graph():
    with open("input.txt", "r") as input_file:
        graph = {}
        root = int(f.readline())
        for line in input_file:
            parent, child = map(int, line.split(","))
            if parent not in graph:
                graph[parent] = []
            graph[parent].append(child)
            if child not in graph:
                graph[child] = []
    return graph, root


def bfs(graph, root):
    queue = deque([(root, 1)])
    visited = {root}
    while queue:
        node, depth = queue.popleft()
        if not graph[node]:
            return depth

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, depth + 1))


def write_result(result):
    with open("output.txt", "w") as output_file:
        o.write(str(result))


def main():
    graph, root = read_graph()
    min_depth = bfs(graph, root)
    write_result(min_depth)


if __name__ == "__main__":
    main()
