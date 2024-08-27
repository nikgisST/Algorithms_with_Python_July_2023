def find_root(parent, node):       # Kruskal's algorithm
    while node != parent[node]:   # parent for 3 is 2 (p[3] = 2), for 2 is 0 (p[2] = 0) and for 0 is 0 (p[0] = 0)
        node = parent[node]
    return node


nodes = int(input())
edges = int(input())
graph = []

for _ in range(edges):
    first, second, weight = [int(x) for x in input().split(' - ')]
    graph.append((first, second, weight))

parent = [n for n in range(nodes)]   # нашите сомостоятелни дървета в началото, всеки един node е дърво само по себе си
total_cost = 0

for first, second, weight in sorted(graph, key=lambda e: e[2]):  #сортиране на рбрата по възходящ ред, first, second, weight - this is unpacked tuple === edges - this is packed tuple
    first_node_root = find_root(parent, first)    # две отделни дървета
    second_node_root = find_root(parent, second)  # две отделни дървета

    if first_node_root == second_node_root: # ако двете стойности са еднакви, имаме едно и също дърво
        continue
    parent[first_node_root] = second_node_root  # ако са различни, имаме две отделни дървета и ги събираме в едно
    total_cost += weight    # това ребро е част от минимално покриващото дърво
    #print(first, second, weight)

print(f'Total cost: {total_cost}')


############################################################################################################


from queue import PriorityQueue    # Prim's algorithm


class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight


def prim(node, graph, forest):
    global total_cost

    forest.add(node)
    pq = PriorityQueue()

    for edge in graph[node]:
        pq.put(edge)

    while not pq.empty():
        min_edge = pq.get()
        non_tree_node = None

        if min_edge.first in forest and min_edge.second not in forest:
            non_tree_node = min_edge.second

        if min_edge.first not in forest and min_edge.second in forest:
            non_tree_node = min_edge.first

        if non_tree_node is None:
            continue

        forest.add(non_tree_node)
        total_cost += min_edge.weight

        for edge in graph[non_tree_node]:
            pq.put(edge)


towns_count = int(input())
roads_count = int(input())

graph = {}

for _ in range(roads_count):
    first, second, weight = [int(x) for x in input().split(' - ')]

    if first not in graph:
        graph[first] = []

    if second not in graph:
        graph[second] = []

    edge = Edge(first, second, weight)
    graph[first].append(edge)
    graph[second].append(edge)

forest = set()
total_cost = 0

for node in graph:
    if node in forest:
        continue

    prim(node, graph, forest)

print(total_cost)
