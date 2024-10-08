def selection_sort(nums):
    for idx in range(len(nums)):
        min_idx = idx  # 0

        for curr_idx in range(idx + 1, len(nums)):
            if nums[curr_idx] < nums[min_idx]:
                min_idx = curr_idx

        nums[idx], nums[min_idx] = nums[min_idx], nums[idx]


nums = [int(x) for x in input().split()]
selection_sort(nums)
print(*nums)


#############################################################################



def selection_sort(nums):
    for idx in range(len(nums)):
        min_number = nums[idx]
        min_idx = idx
        for next_idx in range(idx + 1, len(nums)):
            next_number = nums[next_idx]
            if next_number < min_number:
                min_number = next_number
                min_idx = next_idx
        nums[idx], nums[min_idx] = nums[min_idx], nums[idx]


nums = [int(x) for x in input().split()]
selection_sort(nums)
print(*nums, sep=' ')
