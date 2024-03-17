from typing import List

"""
- container that hold visitedNums 
- loop through the list 
- if the NUMBER is in visitedNums return True and break the loop
- else add the NUMBER to visitedNums
"""


def containsDuplicate(nums: List[int]) -> bool:
    visitedNums = {}

    for i in range(len(nums)):
        currentNum = nums[i]
        if currentNum in visitedNums:
            return True
        else:
            visitedNums[currentNum] = i
    return False


def containsDuplicate2(nums: List[int]) -> bool:
    visitedNums = set()

    for n in nums:
        if n in visitedNums:
            return True
        visitedNums.add(n)
    return False


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4, 7]
    result = containsDuplicate2(prices)
    print(result)
