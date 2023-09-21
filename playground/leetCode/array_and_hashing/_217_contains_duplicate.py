from typing import List

"""
- container that hold visitedNums 
- loop through the list 
- if the NUMBER is in visitedNums return True and break the loop
- else add the NUMBER to visitedNums
"""


def containsDuplicate(nums: List[int]) -> bool:
    visitedNums = {}
    result = False

    for i in range(len(nums)):
        currentNum = nums[i]
        if currentNum in visitedNums:
            result = True
            break
        else:
            visitedNums[currentNum] = i
    return result


def containsDuplicate2(nums: List[int]) -> bool:
    visitedNums = set()

    for n in nums:
        if n in visitedNums:
            return True
        visitedNums.add(n)
    return False
