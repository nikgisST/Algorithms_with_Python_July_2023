def quick_sort(nums, start, end):
    if start >= end:          # ако имаме end по-малък от старта: или имаме масив от 1 елемент, или pointers са разменени и няма какво да се сортира повече
        return         # дъно
    pivot = start
    left= start + 1
    right = end

    while left <= right:
        if nums[left] > nums[pivot] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left] <= nums[pivot]:
            left += 1
        if nums[right] >= nums[pivot]:
            right -= 1

    nums[pivot], nums[right] = nums[right], nums[pivot]

    quick_sort(nums, start, right - 1)    # left sub-array
    quick_sort(nums, right + 1, end)      # right sub-array


nums = [int(x) for x in input().split()]

quick_sort(nums, 0, len(nums) - 1)

print(*nums, sep=' ')