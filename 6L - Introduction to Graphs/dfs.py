# graph represented with dictionary

def dfs(node, graph, visited):
    if node in visited:
        return

    visited.add(node)

    for child in graph[node]:
        dfs(child, graph, visited)

    print(node, end=' ')


graph = {
    1: [19, 21, 14],     # node: list with children
    19: [7, 12, 31, 21],
    7: [1],
    12: [],
    31: [21],
    21: [14],
    14: [6, 23],
    23: [21],
    6: [],
}

visited = set()  # set вместо масив, защото nodes не са последователни

for node in graph:
    dfs(node, graph, visited)


# result: 7 12 6 23 14 21 31 19 1


##################################################################


# graph represented with list

def dfs(node, graph, visited):
    if visited[node]:
        return 

    visited[node] = True

    for child in graph[node]: 
        dfs(child, graph, visited)
 
    print(node, end=' ')


graph = [
    [3, 6],
    [3, 6, 4, 2, 5],
    [1, 4, 5],
    [5, 0, 1],
    [1, 2, 6],
    [2, 1, 3],
    [0, 1, 4]
]

visited = [False] * len(graph)

for node in range(len(graph)):
    dfs(node, graph, visited)


# result: 4 6 1 2 5 3 0 