replace_cost = int(input())    #solution to a subproblem in terms of solutions to smaller acyclic subproblems
insert_cost = int(input())
delete_cost = int(input())
string_a = input()
string_b = input()

rows = len(string_a) + 1
cols = len(string_b) + 1

# for _ in range(rows):
#     dp.append([0] * cols)
dp = [[0] * cols for _ in range(rows)]

for row in range(1, rows):
    dp[row][0] = dp[row - 1][0] + delete_cost

for col in range(1, cols):
    dp[0][col] = dp[0][col - 1] + insert_cost

for row in range(1, rows):
    for col in range(1, cols):
        if string_a[row - 1] == string_b[col - 1]:
            dp[row][col] = dp[row - 1][col - 1]
        else:
            insert = dp[row][col - 1] + insert_cost
            delete = dp[row - 1][col] + delete_cost
            replace = dp[row - 1][col - 1] + replace_cost
            dp[row][col] = min(insert, delete, replace)

#print(f'Minimum edit distance: {dp[-1][-1]}')
print(f'Minimum edit distance: {dp[rows - 1][cols - 1]}')
