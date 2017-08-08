def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        for x in range(i+1, len(nums)):
            if (nums[x] + nums[i] == target):
                return [i, x]

print(twoSum([3,2,4], 6))
