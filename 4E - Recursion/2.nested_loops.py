def loops_with_recursion(idx, nums):
    if idx == n:
        print(*nums, sep=' ')
        return

    for num in range(1, n + 1):
        nums[idx] = num
        loops_with_recursion(idx + 1, nums)


n = int(input())
nums = [None] * n
loops_with_recursion(0, nums)