"""
You are given an integer array height of length n. There are n
vertical lines drawn such that the two endpoints of the i-th line
are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container,
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""
from typing import List


# BRUTE FORCE SOLUTION
def max_area(height: List[int]) -> int:
    res = 0

    for l in range(len(height)):
        for r in range(l + 1, len(height)):
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

    return res


def maxArea(height: List[int]) -> int:
    result = 0
    left, right = 0, len(height) - 1

    while left < right:
        area = (right - left) * min(height[left], height[right])
        result = max(result, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return result


if __name__ == '__main__':
    my_heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    my_result = maxArea(my_heights)
    print(my_result)
