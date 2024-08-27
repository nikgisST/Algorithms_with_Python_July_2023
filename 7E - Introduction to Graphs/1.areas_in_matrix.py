def dfs(parent, row, col, matrix, visited):   # recursive DFS traversal
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        return

    if visited[row][col]:   # if value in visited matrix is with TRUE value
        return

    if matrix[row][col] != parent:
        return

    visited[row][col] = True
    dfs(parent, row + 1, col, matrix, visited)
    dfs(parent, row - 1, col, matrix, visited)
    dfs(parent, row, col + 1, matrix, visited)
    dfs(parent, row, col - 1, matrix, visited)


rows = int(input())
cols = int(input())

matrix = []    # matrix = [list(input()) for _ in range(rows)]
visited = []   # visited = [[False] * cols for _ in range(rows)]

for _ in range(rows):
    matrix.append(list(input()))
    visited.append([False] * cols)

areas = {}
total_areas = 0

for row in range(rows):
    for col in range(cols):
        if visited[row][col]:
            continue

        key = matrix[row][col]
        dfs(key, row, col, matrix, visited)

        if key not in areas:
            areas[key] = 0
        areas[key] += 1

        total_areas += 1

print(f'Areas: {total_areas}')
#[print(f"Letter '{area}' -> {count}") for area, count in sorted(areas.items())]
for area, count in sorted(areas.items()):
    print(f"Letter '{area}' -> {count}")
