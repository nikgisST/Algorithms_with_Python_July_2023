side_a = input().split()
side_b = list(sorted(side_a))

size = len(side_a) + 1
lcs = [[0] * size for _ in range(size)]

for row in range(1, size):
    for col in range(1, size):
        if side_a[row - 1] == side_b[col - 1]:
            lcs[row][col] = lcs[row - 1][col - 1] + 1
        else:
            lcs[row][col] = max(lcs[row][col - 1], lcs[row - 1][col])

print(f'Maximum pairs connected: {lcs[-1][-1]}')
