"""
Given an unsorted array of integers nums,
return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""

from typing import List


def longestConsecutive(nums: List[int]) -> int:
    numsSet = set(nums)
    longest = 0

    for n in numsSet:
        if (n - 1) not in numsSet:
            length = 0
            while (n + length) in numsSet:
                length += 1
            longest = max(longest, length)
    return longest


def longestConsecutive2(nums: List[int]) -> int:
    result = 0
    new_nums = set(nums)

    for num in new_nums:
        count = 0

        prev = num - 1
        if prev in new_nums:
            continue
        else:
            count += 1
            nxt = num + 1
            while nxt in new_nums:
                count += 1
                nxt += 1

            result = max(result, count)

    return result


if __name__ == '__main__':
    my_nums = [100, 4, 200, 1, 3, 2]
    my_target = 9
    rsl = longestConsecutive(my_nums)
    print(rsl)
