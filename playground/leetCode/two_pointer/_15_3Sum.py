"""
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
   such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

   Notice that the solution set must not contain duplicate triplets.

"""
from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()  # O(n)
    result = []

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue

        l = i + 1
        r = len(nums) - 1

        while l < r:
            threesum = nums[i] + nums[l] + nums[r]
            if threesum > 0:
                r -= 1
            elif threesum < 0:
                l += 1
            else:
                result.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return result
