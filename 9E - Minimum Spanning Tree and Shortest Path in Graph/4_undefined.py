from collections import deque           # shortest paths in graph: Bellman-Ford


def find_path(parent, node):
    current_path = deque()
    while node is not None:
        current_path.appendleft(node)
        node = parent[node]      # node да стане предишния node
    return current_path


nodes = int(input())
edges = int(input())
graph = []
####################### Bellman-Ford ###########################
for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split()]
    graph.append((source, destination, weight))

start = int(input())
target = int(input())

distance = [float('inf')] * (nodes + 1)
distance[start] = 0

parent = [None] * (nodes + 1)

for _ in range(nodes - 1):    # (v - 1) times
    for source, destination, weight in graph:
        if distance[source] == float('inf'):   # няма нито един открит път, започващ от първия node
            continue
        new_distance = distance[source] + weight
        if new_distance < distance[destination]:
            distance[destination] = new_distance
            parent[destination] = source       # за да стигнем до дестинацията, трябва да минем през източника
####################### Bellman-Ford ###########################

for source, destination, weight in graph:     # втори loop при Bellman-Ford, ако се намери нова по-добра дистанция, влизаме в негативен цикъл
    new_distance = distance[source] + weight
    if new_distance < distance[destination]:
        print('Undefined')
        break
else:
    path = find_path(parent, target)
    print(*path, sep=' ')
    print(distance[target])
