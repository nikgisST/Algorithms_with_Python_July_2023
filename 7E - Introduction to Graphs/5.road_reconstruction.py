def dfs(node, graph, visited):   # solution with DFS and array
    if visited[node]:
        return

    visited[node] = True
    for child in graph[node]:
        dfs(child, graph, visited)


nodes_count = int(input())
edges_count = int(input())

graph = []
[graph.append([]) for _ in range(nodes_count)]
edges = []

for _ in range(edges_count):
    first, second = [int(x) for x in input().split(' - ')]
    graph[first].append(second)
    graph[second].append(first)
    edges.append((min(first, second), max(first, second)))

print("Important streets:")

for first, second in sorted(edges, key=lambda t: (t[0], t[1])):
    graph[first].remove(second)
    graph[second].remove(first)

    visited = [False] * nodes_count

    dfs(0, graph, visited)

    if not all(visited):
        print(f'{first} {second}')

    graph[first].append(second)
    graph[second].append(first)


##################################################################################################


def dfs(node, destination, town, visited):  # solution with DFS and dictionary
    if node in visited:
        return

    visited.add(node)
    if node == destination:
        return

    for child in town[node]:
        dfs(child, destination, town, visited)


def not_path(source, destination, town):
    visited = set()
    dfs(source, destination, town, visited)

    return destination not in visited


buildings_count = int(input())
streets_count = int(input())
town = {}
streets = []

for _ in range(streets_count):
    source, destination = input().split(' - ')
    streets.append((source, destination))
    streets.append((destination, source))

    if source not in town:
        town[source] = []
    town[source].append(destination)

    if destination not in town:
        town[destination] = []
    town[destination].append(source)

important_streets = []

for source, destination in sorted(streets, key=lambda x: (x[0], x[1])):
    if source not in town[destination] or destination not in town[source]:
        continue

    town[source].remove(destination)
    town[destination].remove(source)

    if not_path(source, destination, town):
        important_streets.append((source, destination))
    else:
        town[source].append(destination)
        town[destination].append(source)

print('Important streets:')
#[print(f'{source} {destination}') for source, destination in important_streets]
for source, destination in important_streets:
    print(f'{source} {destination}')
