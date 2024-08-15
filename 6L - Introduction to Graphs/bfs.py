from collections import deque


def bfs(node, graph, visited):
    if node in visited:
        return 

    queue = deque([node])  # стартовия node, от който тръгваме да обхождаме
    visited.add(node)

    while queue:
        current_node = queue.popleft()
        print(current_node, end=' ')

        for child in graph[current_node]:  # минаваме през всички деца на текущия node
            if child not in visited:
                visited.add(child)
                queue.appen(child)   # добавяме го, за да можем в даден момент да го обходим


graph = {
    7: [19, 21, 14],
    19: [1, 12, 31, 21],
    1: [7],
    12: [],
    31: [21],
    21: [14],
    14: [23, 6],
    6: [],
    23: [21]
}

visited = set()  # set вместо масив, защото nodes не са последователни

for node in graph:
    bfs(node, graph, visited)


# result: 7 19 21 14 1 12 31 23 6 