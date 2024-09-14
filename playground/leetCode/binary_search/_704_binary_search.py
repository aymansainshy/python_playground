from typing import List

"""
Given an array of integers nums which is sorted in ascending order,
and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

"""


# Use Binary search when array is sorted

def binary_search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        # middle = (left + right) // 2
        middle = left + ((right - left) // 2)
        if target > nums[middle]:
            left = middle + 1
        elif target < nums[middle]:
            right = middle - 1
        else:
            return middle
    return -1


if __name__ == '__main__':
    nums_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    my_target = 2

    founded = binary_search(nums_list, my_target)
    print(founded)
