from typing import List


def binary_search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        # middle = (right + left) // 2
        middle = left + ((left - right) // 2)
        if target < nums[middle]:
            right = middle - 1
        elif target > nums[middle]:
            left = middle + 1
        else:
            return middle
    return -1


if __name__ == '__main__':
    nums_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    my_target = 9

    founded = binary_search(nums_list, my_target)
    print(founded)
