def dfs(node, graph, visited, cycles):   # topological sorting: DFS algorithm + cycle detection
    if node in cycles:
        raise Exception
    if node in visited:
        return

    visited.add(node)
    cycles.add(node)

    for child in graph[node]:
        dfs(child, graph, visited, cycles)

    cycles.remove(node)


graph = {}
while True:
    line = input()
    if line == 'End':
        break

    source, destination = line.split('-')
    if source not in graph:     # KEY
        graph[source] = []
    if destination not in graph:   # VALUE
        graph[destination] = []

    graph[source].append(destination)

visited = set()

try:
    for node in graph:
        dfs(node, graph, visited, set())
    print('Acyclic: Yes ')

except Exception:
    print('Acyclic: No')


###########################################################################################

def find_dependencies(graph):   # topological sorting: source removal algorithm
    result = {}

    for node, childs in graph.items():
        if node not in result:
            result[node] = 0

        for child in childs:
            if child not in result:
                result[child] = 1
            else:
                result[child] += 1
    return result


def find_node_without_dependencies(dependencies):
    for node, depend in dependencies.items():
        if depend == 0:
            return node
    return None


graph = {}
while True:
    line = input()
    if line == 'End':
        break

    node, child = line.split('-')

    if node not in graph:
        graph[node] = []
    graph[node].append(child)

dependencies = find_dependencies(graph)
has_cycle = False

while dependencies:
    node_to_remove = find_node_without_dependencies(dependencies)

    if not node_to_remove:
        has_cycle = True
        break

    if node_to_remove in graph:
        for child in graph[node_to_remove]:
            dependencies[child] -= 1
    dependencies.pop(node_to_remove)

if has_cycle:
    print('Acyclic: No')
else:
    print('Acyclic: Yes')
