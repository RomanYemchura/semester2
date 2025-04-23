with open("govern.in.txt", "r") as file:
    lines = file.readlines()
    before = {}
    in_degree = {}
    for line in lines:
        a, b = line.strip().split()
        if b not in before:
            before[b] = []
        before[b].append(a)
        in_degree[a] = in_degree.get(a, 0) + 1

        if b not in in_degree:
            in_degree[b] = 0
queue = []
for doc in in_degree:
    if in_degree[doc] == 0:
        queue.append(doc)

order = []

while queue:
    current = queue.pop()
    order.append(current)

    if current in before:
        for dependent in before[current]:

            in_degree[dependent] -= 1
            if in_degree[dependent] == 0:
                queue.append(dependent)

with open("govern.out.txt", "w") as file:
    for doc in order:
        file.write(doc + "\n")
