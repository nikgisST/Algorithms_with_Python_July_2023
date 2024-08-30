def dfs(node, graph, visited_nodes):    # Solution with DFS and dictionary as graph
    if node in visited_nodes:    # if node not in unvisited_nodes:
        return

    visited_nodes.add(node)    # unvisited_nodes.remove(node)
    for child in graph[node]:
        dfs(child, graph, visited_nodes)   # dfs(child, graph, unvisited_nodes)


nodes = int(input())
edges = int(input())
graph = {node: [] for node in range(1, nodes + 1)}

for _ in range(edges):
    source, destination = [int(x) for x in input().split()]
    graph[source].append(destination)

start_node = int(input())
visited = set()                      # без този сет, всичко се съдържа в лист unvisited_nodes
dfs(start_node, graph, visited)      # dfs(start_node, graph, unvisited_nodes)

unreachable_nodes = []      # unreachable_nodes = list(graph.keys())
for node in graph.keys():                # for node in graph.keys():
    if node not in visited:              #     unvisited_nodes.append(node)
        unreachable_nodes.append(node)

print(*sorted(unreachable_nodes), sep=' ')      # print(*unvisited_nodes, sep=' ')


#################################################################################################


def dfs(node, graph, unvisited_nodes):  # Solution with DFS and list as graph
    if node not in unvisited_nodes:
        return

    unvisited_nodes.remove(node)
    for child in graph[node]:
        dfs(child, graph, unvisited_nodes)


nodes = int(input())
edges = int(input())
graph = [[] for x in range(nodes + 1)]

for _ in range(edges):
    source, destination = [int(x) for x in input().split()]
    graph[source].append(destination)

start_node = int(input())
unvisited_nodes = list(x for x in range(1, nodes + 1))
dfs(start_node, graph, unvisited_nodes)

print(*unvisited_nodes, sep=' ')


