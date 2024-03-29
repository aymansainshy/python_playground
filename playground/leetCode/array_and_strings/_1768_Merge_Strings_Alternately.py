"""
You are given two array_and_strings word1 and word2.
Merge the array_and_strings by adding letters in alternating order,
starting with word1. If a string is longer than the other,
append the additional letters onto the end of the merged string.

Return the merged string.
"""


def mergeAlternately(word1: str, word2: str) -> str:
    i, j = 0, 0
    result = []

    while i < len(word1) and j < len(word2):
        result.append(word1[i])
        result.append(word2[j])
        i += 1
        j += 1
    # add the remaining letters
    result.append(word1[i:])
    result.append(word2[j:])

    return ''.join(result)


if __name__ == '__main__':
    word_1 = "abc"
    word_2 = "pqrMOV"

    my_result = mergeAlternately(word_1, word_2)
    print(my_result)
