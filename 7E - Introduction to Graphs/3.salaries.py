def dfs(employee, graph, salaries):
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


employees_count = int(input())
graph = []

for _ in range(employees_count):
    line = input()
    children = []
    for idx, state in enumerate(line):
        if state == 'Y':
            children.append(idx)

    graph.append(children)

salaries = [None] * employees_count
total_salary = 0

for employee in range(employees_count):
    current_salary = dfs(employee, graph, salaries)
    total_salary += current_salary

print(total_salary)