def searchRange(self, nums: List[int], target: int) -> List[int]:
    l = 0
    r = len(nums) - 1
    search = -1
    while (l <= r):
        mid = (l + r) // 2
        if (nums[mid] < target):
            l = mid + 1
        elif (nums[mid] == target):
            search = mid
            break
        else:
            r = mid - 1
    if (search == -1):
        return [-1, -1]

    left_part = -1
    right_part = -1
    l = 0
    r = search - 1

    while (l <= r):
        mid = (l + r) // 2
        if (nums[mid] < target):
            l = mid + 1
        elif (nums[mid] == target):
            left_part = mid
            r = mid - 1
        else:
            r = mid - 1
    if (left_part == -1):
        left_part = search
    l = search + 1
    r = len(nums) - 1
    while (l <= r):
        mid = (l + r) // 2
        if (nums[mid] < target):
            l = mid + 1
        elif (nums[mid] == target):
            right_part = mid
            l = mid + 1
        else:
            r = mid - 1
    if (right_part == -1):
        right_part = search
    return [left_part, right_part]


