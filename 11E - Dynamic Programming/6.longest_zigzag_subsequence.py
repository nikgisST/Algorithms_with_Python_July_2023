from collections import deque     # Longest Increasing Subsequence


nums = [int(x) for x in input().split()]

dp = []
[dp.append([0] * len(nums)) for _ in range(2)]      #dp = [[0] * len(nums) for _ in range(2)]

parent = []
[parent.append([None] * len(nums)) for _ in range(2)]   #parent = [[None] * len(nums) for _ in range(2)]

dp[0][0] = dp[1][0] = 1   # base case - базовото решение

best_size = 0
best_row = 0
best_col = 0

for current_idx in range(1, len(nums)):
    current_number = nums[current_idx]
    for prev_idx in range(current_idx - 1, -1, -1):
        prev_number = nums[prev_idx]

        if current_number > prev_number and dp[1][prev_idx] + 1 >= dp[0][current_idx]:
            dp[0][current_idx] = dp[1][prev_idx] + 1
            parent[0][current_idx] = prev_idx

        if current_number < prev_number and dp[0][prev_idx] + 1 >= dp[1][current_idx]:
            dp[1][current_idx] = dp[0][prev_idx] + 1
            parent[1][current_idx] = prev_idx

    if dp[0][current_idx] > best_size:
        best_size = dp[0][current_idx]
        best_row = 0
        best_col = current_idx

    if dp[1][current_idx] > best_size:
        best_size = dp[1][current_idx]
        best_row = 1
        best_col = current_idx

result = deque()
while best_col is not None:
    result.appendleft(nums[best_col])
    best_col = parent[best_row][best_col]
    best_row = 1 if best_row == 0 else 0

print(*result, sep=' ')
