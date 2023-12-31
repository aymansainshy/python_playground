"""
   Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
   find two numbers such that they add up to a specific target number.
   Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

   Return the indices of the two numbers, index1 and index2,
   added by one as an integer array [index1, index2] of length 2.

   The tests are generated such that there is exactly one solution.
   You may not use the same element twice.

   Your solution must use only constant extra space.
"""
from typing import List

"""
 [1, 2, 7, 9, 11, 15] // 13
 - l pointer to smallest numbers
 - r pointer to largest numbers
 - while sum of two pointer > than target / decrease r els increase l
 
"""


def twoSum2(numbers: List[int], target: int) -> List[int]:
    left = 0
    right = len(numbers) - 1

    while left < right:
        curSum = numbers[left] + numbers[right]

        if curSum > target:
            right -= 1
        elif curSum < target:
            left += 1
        else:
            return [left + 1, right + 1]
