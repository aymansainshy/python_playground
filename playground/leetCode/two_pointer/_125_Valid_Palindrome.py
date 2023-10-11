"""
A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""


def isPalindrome(s: str) -> bool:
    new_string = string_transformer(s)

    print(new_string)

    l = 0
    r = len(new_string) - 1

    while l < r:
        if new_string[l] != new_string[r]:
            return False

        l += 1
        r -= 1

    return True


def string_transformer(s: str) -> str:
    new_string = ""

    for char in s:
        if char.isalpha() or char.isdigit():  # char.is_alnum()
            new_string += char

    return new_string.lower()
