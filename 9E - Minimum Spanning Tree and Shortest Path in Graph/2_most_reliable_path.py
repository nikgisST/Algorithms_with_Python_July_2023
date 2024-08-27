from collections import deque       # shortest paths in graph: Dijkstra's algorithm
from queue import PriorityQueue

# class Node:
#     def __init__(self, value, distance):
#         pass
#     def __gt__(self, other):
#         return self.distance > other.distance

class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight


nodes = int(input())
edges = int(input())
graph = []
[graph.append([]) for _ in range(nodes)]    # [None, None, None, None, None, None, None]  === count of nodes

for _ in range(edges):
    first, second, weight = [int(x) for x in input().split()]
    edge = Edge(first, second, weight)
    graph[first].append(edge)
    graph[second].append(edge)

start_node = int(input())
target_node = int(input())

pq = PriorityQueue()
pq.put((-100, start_node))   # -100 е началната дистанция за стартовия node

distance = [float('-inf')] * nodes
distance[start_node] = 100

parent = [None] * nodes

while not pq.empty():
    max_distance, node = pq.get()

    if node == target_node:
        break

    for edge in graph[node]:
        child = edge.second if edge.first == node else edge.first
        new_distance = -max_distance * edge.weight / 100    # -max_distance - минусът го обръщаме на плюс
        if new_distance > distance[child]:
            distance[child] = new_distance
            parent[child] = node
            pq.put((-new_distance, child))   # -max_distance - а като влизат в опашката ги обръщаме с минус

print(f'Most reliable path reliability: {distance[target_node]:.2f}%')

path = deque()
node = target_node
while node is not None:
    path.appendleft(node)
    node = parent[node]

print(*path, sep=' -> ')
