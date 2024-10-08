def find_path(node, parent):     #  Bellman-Ford
    first_node = node
    result = [node]
    while True:
        node = parent[node]
        result.append(node)
        if node == first_node:
            break
    return result[::-1]


nodes = set()
edges = int(input())
graph = []
for _ in range(edges):
    source, destination, weight_as_string = input().split()
    weight = float(weight_as_string)
    graph.append((source, destination, weight))
    nodes.add(source)
    nodes.add(destination)

start_node = input()
distance = {node: float('-inf') for node in nodes}
distance[start_node] = 1
parent = {node: None for node in nodes}

############################### BELLMAN-FORD ####################################
for _ in range(len(nodes) - 1):           # (v - 1) times
    for (source, destination, weight) in graph:
        new_distance = distance[source] * weight
        if new_distance > distance[destination]:
            distance[destination] = new_distance
            parent[destination] = source    # за да стигнем до дестинацията, трябва да минем през източника

for (source, destination, weight) in graph:    # втори loop при Bellman-Ford, ако се намери нова по-добра дистанция, влизаме в негативен цикъл
    new_distance = distance[source] * weight
    if new_distance > distance[destination]:
        print(True)
        path = find_path(start_node, parent)
        print(*path, sep=' ')
        break
############################### BELLMAN-FORD ####################################
else:
    print(False)
    for node, best_price in distance.items():
        print(f"{node}: {best_price:.3f}")
