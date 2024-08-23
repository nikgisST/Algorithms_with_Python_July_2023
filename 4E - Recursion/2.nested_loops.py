def nested_loops(idx, arr):
    if idx >= len(arr):
        print(*arr, sep=' ')
        return

    for num in range(1, len(arr) + 1):
        arr[idx] = num
        nested_loops(idx + 1, arr)


n = int(input())
arr = [None] * n
nested_loops(0, arr)

############################################################

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
