import csv
import heapq


def read_matrix():
    with open("islands.csv", "r") as f:
        reader = csv.reader(f)

        matrix = [list(map(int, row)) for row in reader]

    return matrix


def minimum_spanning_tree(matrix):
    n = len(matrix)
    if n >= 100:
        print(f"Занадто багато вузлів")
    elif n <= 1:
        print(f"Замало вулів для обчислення")
    else:
        print(f"Усього вузлів : {n}")

    visited = []

    for i in range(n):
        visited.append(False)

    min_edge = [(0, 0)]
    total_cost = 0

    while min_edge:

        cost, u = heapq.heappop(min_edge)
        if visited[u]:
            continue

        visited[u] = True
        total_cost += cost

        for v in range(n):
            if not visited[v] and matrix[u][v] > 0:
                heapq.heappush(min_edge, (matrix[u][v], v))

    return total_cost


if __name__ == "__main__":
    matrix = read_matrix()
    result = minimum_spanning_tree(matrix)
    print(f"Найменша давжина кабелю : {result}")
    
