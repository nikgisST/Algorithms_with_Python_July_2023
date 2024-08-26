def dfs(employee, graph, salaries):       # employee === node
    if salaries[employee] is not None:
        return salaries[employee]

    if len(graph[employee]) == 0:
        salaries[employee] = 1
        return 1

    salary = 0
    for child in graph[employee]:
        salary += dfs(child, graph, salaries)

    salaries[employee] = salary
    return salary


nodes = int(input())    # employees count
graph = []

for _ in range(nodes):
    line = input()
    children = []
    for idx, state in enumerate(line):
        if state == 'Y':
            children.append(idx)
    graph.append(children)

salaries = [None] * nodes
total_salary = 0

for employee in range(nodes):
    current_salary = dfs(employee, graph, salaries)
    total_salary += current_salary

print(total_salary)
