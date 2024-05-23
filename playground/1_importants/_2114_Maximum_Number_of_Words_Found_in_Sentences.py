"""
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

You are given an array of strings sentences, where each sentences[i] represents a single sentence.

Return the maximum number of words that appear in a single sentence.

Example 1:
Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
Output: 6
Explanation:
- The first sentence, "alice and bob love leetcode", has 5 words in total.
- The second sentence, "i think so too", has 4 words in total.
- The third sentence, "this is great thanks very much", has 6 words in total.
Thus, the maximum number of words in a single sentence comes from the third sentence, which has 6 words.

Example 2:
Input: sentences = ["please wait", "continue to fight", "continue to win"]
Output: 3
Explanation: It is possible that multiple sentences contain the same number of words.
In this example, the second and third sentences (underlined) have the same number of words.

Constraints:

1 <= sentences.length <= 100
1 <= sentences[i].length <= 100
sentences[i] consists only of lowercase English letters and ' ' only.
sentences[i] does not have leading or trailing spaces.
All the words in sentences[i] are separated by a single space.
"""
from typing import List


def mostWordsFound(sentences: List[str]) -> int:
    max_res = 0

    for sentence in sentences:
        words = sentence.split(" ")

        max_res = max(max_res, len(words))

    return max_res


# From Interview
def mostWordsFound2(sentences: List[str]) -> str:
    max_result = 0
    map_count = {}

    for sent in sentences:
        new_words_array = sent.split(" ")

        max_result = max(max_result, len(new_words_array))
        map_count[len(new_words_array)] = sent

    return f"{max_result} : {map_count[max_result]}"


if __name__ == '__main__':
    sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]

    result = mostWordsFound(sentences)
    print(result)

    # result = mostWordsFound2(sentences)
    # print(result)
