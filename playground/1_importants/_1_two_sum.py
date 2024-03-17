from typing import List

"""
- container that hold visitedNums
- loop through the list 
- look for the needed number 
- if the NUMBER is in visitedNums return the index of it and the current number index
- else add the number and it's index to visited numbers
"""


def twoSum(nums: List[int], target: int) -> List[int]:
    visitedChars = {}

    for i in range(len(nums)):
        currentNum = nums[i]
        neededNum = target - currentNum

        if neededNum in visitedChars:
            index2 = visitedChars[neededNum]
            return [index2, i]
        else:
            visitedChars[currentNum] = i

    return []


if __name__ == '__main__':
    my_nums = [2, 7, 11, 15]
    my_target = 9
    result = twoSum(my_nums, my_target)
    print(result)
