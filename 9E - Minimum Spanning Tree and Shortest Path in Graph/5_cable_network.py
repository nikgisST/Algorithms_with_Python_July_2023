from queue import PriorityQueue

####################### Prim's ###########################
class Edge:
    def __init__(self, start, end, weight):
        self.first = start
        self.second = end
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight


budget = int(input())
nodes = int(input())
edges = int(input())
forest = set()
budget_used = 0

graph = []
[graph.append([]) for _ in range(nodes)]

for _ in range(edges):
    edge_data = input().split()
    first, second, weight = int(edge_data[0]), int(edge_data[1]), int(edge_data[2])
    
    edge = Edge(first, second, int(weight))
    graph[first].append(edge)
    graph[second].append(edge)

    if 'connected' in edge_data:    # if len(edge_data) == 4:
        forest.add(first)
        forest.add(second)

pq = PriorityQueue()
for node in forest:            # add all edges which are connected already
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
    for edge in graph[non_tree_node]:
        pq.put(edge)
####################### Prim's ###########################

    if budget_used + min_edge.weight > budget:
        break
    budget_used += min_edge.weight
print(f'Budget used: {budget_used}')
