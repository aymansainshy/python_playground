from leetCode.sliding_window._121_best_time_to_buy_and_sell_stock import maxProfit
from leetCode.array_and_hashing._217_contains_duplicate import containsDuplicate2
from leetCode.array_and_hashing._1_two_sum import twoSum
from leetCode.array_and_hashing._49_groub_anagram import groupAnagrams
from leetCode.two_pointer._167_two_sum_II_input_array_is_sorted import twoSum2
from leetCode.two_pointer._125_Valid_Palindrome import isPalindrome
from leetCode.two_pointer._15_3Sum import threeSum

if __name__ == '__main__':
    # nums = [-1, 0, 1, 2, -1, -4]
    # result = threeSum(nums)
    # print(result)
    #

    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = groupAnagrams(strs)
    print(result)

    # myString = "0P"
    # result = isPalindrome(myString)
    # print(result)

    # myString = "sainshy"
    # result = Solution.lengthOfLongestSubstring(myString)
    # print(result)

    # prices = [7, 1, 5, 3, 6, 4]
    # max_profit = maxProfit(prices)
    # print(max_profit)

    # prices = [7, 1, 5, 3, 6, 4, 7]
    # result = containsDuplicate2(prices)
    # print(result)

    # s = "anagram"
    # t = "nagaram"
    #
    # result = isAnagram(s, t)
    # print(result)

    # nums = [2, 7, 11, 15]
    # target = 9
    # result = twoSum(nums, target)
    # print(result)

    # numbers =[1]
    # target = 1
    # result = twoSum2(numbers, target)
    # print(result)
