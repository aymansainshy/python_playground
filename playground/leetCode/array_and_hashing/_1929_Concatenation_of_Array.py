"""
 Given an integer array nums of length n, you want to create an array ans of
 length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

 Specifically, ans is the concatenation of two nums arrays.

 Return the array ans.

 Example 1:
 Input: nums = [1,2,1]
 Output: [1,2,1,1,2,1]
 Explanation: The array ans is formed as follows:
 - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
 - ans = [1,2,1,1,2,1]

 Example 2:
 Input: nums = [1,3,2,1]
 Output: [1,3,2,1,1,3,2,1]
 Explanation: The array ans is formed as follows:
 - ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
 - ans = [1,3,2,1,1,3,2,1]
"""
from typing import List


def getConcatenation(nums: List[int]) -> List[int]:
    ans = [0] * 2 * len(nums)  # [0,0,0,0,0,0,0,0] if nums length is 4

    for i in range(len(nums)):
        ans[i] = nums[i]
        ans[i + len(nums)] = nums[i]

    return ans


def getConcatenation2(nums: List[int]) -> List[int]:
    nums1 = nums
    nums2 = nums

    ans = nums1 + nums2

    return ans


def getConcatenation3(nums: List[int]) -> List[int]:
    ans = []

    for i in range(2):
        for n in nums:
            ans.append(n)

    return ans


if __name__ == '__main__':
    nums_list = [1, 3, 2, 1]

    ans_1 = getConcatenation(nums_list)
    ans_2 = getConcatenation2(nums_list)
    ans_3 = getConcatenation3(nums_list)

    print(ans_1)
    print(ans_2)
    print(ans_3)
