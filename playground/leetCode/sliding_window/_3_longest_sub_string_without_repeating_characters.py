def lengthOfLongestSubstring2(s: str) -> int:
    result = 0
    visitedChar = set()
    left = 0  # sainshy
    right = 0

    # for right in range(len(s)):
    while right < len(s):
        while s[right] in visitedChar:
            visitedChar.remove(s[left])
            left += 1

        visitedChar.add(s[right])
        result = max(result, len(visitedChar))
        right += 1

    return result


#


def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 1:
        return 1

    result = 0

    lonSubString = ""  # "sainshy"

    start = 0
    end = 1
    if len(s) > 0:
        lonSubString += s[start]

    while end < len(s):
        nextChar = s[end]
        if nextChar in lonSubString:
            result = max(result, len(lonSubString))
            lonSubString = ""
            start += 1
            end = start + 1
            lonSubString += s[start]
        else:
            lonSubString += s[end]
            end += 1

        result = max(result, len(lonSubString))
    return result


if __name__ == '__main__':
    result = lengthOfLongestSubstring2(' ')
    print(result)
