def array_sum(nums, idx):
    if idx == len(nums) - 1:          # дъно на рекурсията
        return nums[idx]

    return nums[idx] + array_sum(nums, idx + 1)


# 1 2 3 4 5
nums = [int(x) for x in input().split()]

print(array_sum(nums, 0))