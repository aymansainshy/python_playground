"""
   If you gaven and array of sentences
   return the sentences that contain the max number of words  with words count

   words = ["alice and bob love code", "i think so too", "this is greate thanks very much"];
"""
from typing import List


def longestSentence(sentences: List[str]) -> str:
    max_result = 0
    map_count = {}

    for sent in sentences:
        new_words_array = sent.split(" ")

        max_result = max(max_result, len(new_words_array))
        map_count[len(new_words_array)] = sent

    return f"{max_result} : {map_count[max_result]}"


if __name__ == '__main__':
    words = ["alice and bob love code", "i think so too", "this is greate thanks very much"]

    result = longestSentence(words)
    print(result)
