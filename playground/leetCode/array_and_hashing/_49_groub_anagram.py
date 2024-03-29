"""
 Given an array of array_and_strings strs, group the anagrams together.
 You can return the answer in any order.

 An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
 typically using all the original letters exactly once.
"""
from collections import defaultdict
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    dic = defaultdict(list)

    for word in strs:
        lst = [0] * 26  # [0,0,0,0,0,0,0,0,0 .... etc 26 Zeros]
        for char in word:
            lst[ord(char) - ord('a')] += 1

        lst = tuple(lst)
        dic[lst].append(word)

    return dic.values()


def groupAnagrams2(strs: List[str]) -> List[List[str]]:
    dic = defaultdict(list)
    # {
    #     'word': ['word1', 'word2']
    # }

    for word in strs:
        dic[tuple(sorted(word))].append(word)

    return dic.values()


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = groupAnagrams(strs)
    print(result)
