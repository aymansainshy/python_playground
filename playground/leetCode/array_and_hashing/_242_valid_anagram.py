"""
  Given two strings s and t, return true if t is an anagram of s, and false otherwise.

  An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
  typically using all the original letters exactly once.

  Example 1:

  Input: s = "anagram", t = "nagaram"
  Output: true
  Example 2:

  Input: s = "rat", t = "car"
  Output: false
"""
"""
  - check if the length of the two string equal
  - count the character for each String
  - if char is not in sCount return False
  - if ScharCount != TcharCount return False
  - else return True 
"""


def isAnagram(s: str, t: str) -> bool:
    # Solution 1 - O(N)
    if len(s) != len(t):
        return False

    sCount = charCount(s)
    tCount = charCount(t)

    for char in tCount:
        if char not in sCount:
            return False

        if tCount[char] != sCount[char]:
            return False

    return True

    # Solution 2 - O(1)
    # return sorted(s) == sorted(t)


def charCount(s: str) -> dict[str, int]:
    visitedChar = {}

    for char in s:
        if char in visitedChar:
            visitedChar[char] += 1
        else:
            visitedChar[char] = 1

    return visitedChar
