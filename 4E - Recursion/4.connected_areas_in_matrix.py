class Area:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size


def explore_area(row, col, matrix):
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        return 0

    if matrix[row][col] != '-':     # ИЛИ == '*' ИЛИ == 'v'   if matrix[row][col] != EMPTY:
        return 0

    matrix[row][col] = "v"      # matrix[row][col] = VISITED

    result = 1
    result += explore_area(row - 1, col, matrix)  # down    child 1
    result += explore_area(row + 1, col, matrix)  # up      child 2
    result += explore_area(row, col + 1, matrix)  # right   child 3
    result += explore_area(row, col - 1, matrix)  # left    child 4

    return result


rows = int(input())
cols = int(input())

matrix = []              # matrix = [[x for x in input()] for _ in range(rows)]
for _ in range(rows):
    matrix.append(list(input()))        #print(matrix)   лист от листове
# EMPTY, WALL, VISITED = '-', '*', 'v'


areas = []   # list of tuples to store founded areas

for row in range(rows):
    for col in range(cols):
        size = explore_area(row, col, matrix)
        if size == 0:
            continue
        # if size:
        areas.append(Area(row, col, size))

print(f'Total areas found: {len(areas)}')
for idx, area in enumerate(sorted(areas, key=lambda a: a.size, reverse=True)):   #(areas, key=lambda a: -a.size)
    print(f'Area #{idx + 1} at ({area.row}, {area.col}), size: {area.size}')


#########################################################################


def explore_area(row, col, matrix):
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        return 0

    if matrix[row][col] != '-':     # ИЛИ == '*' ИЛИ == 'v'   if matrix[row][col] != EMPTY:
        return 0

    matrix[row][col] = "v"      # matrix[row][col] = VISITED

    result = 1
    result += explore_area(row - 1, col, matrix)  # down    child 1
    result += explore_area(row + 1, col, matrix)  # up      child 2
    result += explore_area(row, col + 1, matrix)  # right   child 3
    result += explore_area(row, col - 1, matrix)  # left    child 4

    return result


rows = int(input())
cols = int(input())

matrix = [[x for x in input()] for _ in range(rows)]
# EMPTY, WALL, VISITED = '-', '*', 'v'

areas = []   # list of tuples to store founded areas

for row in range(rows):
    for col in range(cols):
        size = explore_area(row, col, matrix)
        if size == 0:
            continue
        # if size:
        areas.append((row, col, size))

print(f'Total areas found: {len(areas)}')
for idx, (row, col, size) in enumerate(sorted(areas, key=lambda a: -a[2])):
    print(f'Area #{idx + 1} at ({row}, {col}), size: {size}')
