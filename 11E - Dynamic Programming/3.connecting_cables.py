cables = [int(x) for x in input().split()]     # Longest Common Subsequence

size = len(cables) + 1
positions = [pos for pos in range(1, size)]

lcs = [[0] * size for _ in range(size)]

for row in range(1, size):
    for col in range(1, size):
        if cables[row - 1] == positions[col - 1]:      # ако са еднакви последните два добавени елемента в двета събсета
            lcs[row][col] = lcs[row - 1][col - 1] + 1   # гледаме предишния state на двата subsequence и добавяме 1
        else:
            lcs[row][col] = max(lcs[row][col - 1], lcs[row - 1][col])  # иначе гледаме и в единия, и в другия и взимаме най-големият с общи преднидни елементи

#print(f'Maximum pairs connected: {lcs[-1][-1]}')
print(f'Maximum pairs connected: {lcs[size - 1][size - 1]}')
