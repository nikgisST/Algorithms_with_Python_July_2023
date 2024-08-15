def bubble_sort(nums):
    is_sorted = False
    i_counter = 0

    while not is_sorted:
        is_sorted = True

        for j in range(1, len(nums) - i_counter):
        # for j in range(0, len(nums) - i_counter - 1):
            if nums[j - 1] > nums[j]:
            # if nums[j + 1] > nums[j]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                is_sorted = False

        i_counter += 1


nums = [int(x) for x in input().split()]
bubble_sort(nums)
print(*nums)