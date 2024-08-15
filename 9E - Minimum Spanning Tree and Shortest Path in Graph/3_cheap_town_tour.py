Solved with Kruskal algorithm

def find_root(parent, node):
    while node != parent[node]:
        node = parent[node]
    return node


towns_count = int(input())
roads_count = int(input())

graph = []

for _ in range(roads_count):
    first, second, weight = [int(x) for x in input().split(' - ')]
    graph.append((first, second, weight))

parent = [n for n in range(towns_count)]
total_cost = 0

for first, second, weight in sorted(graph, key=lambda e: e[2]):
    first_node_root = find_root(parent, first)
    second_node_root = find_root(parent, second)

    if first_node_root != second_node_root:
        parent[first_node_root] = second_node_root
        total_cost += weight

print(f'Total cost: {total_cost}')



######################################################################



Solved with Prim's Algorithm

from queue import PriorityQueue


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