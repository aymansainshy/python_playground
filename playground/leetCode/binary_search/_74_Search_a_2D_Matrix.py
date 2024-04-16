"""
You are given an m x n integer matrix, matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""

from typing import List


def searchMatrix3(matrix: List[List[int]], target: int) -> bool:
    top, bottom = 0, len(matrix) - 1

    while top <= bottom:
        mid_row = (bottom + top) // 2
        if target > matrix[mid_row][-1]:
            top = mid_row + 1
        elif target < matrix[mid_row][0]:
            bottom = mid_row - 1
        else:
            break

    if not (top <= bottom):
        return False

    row = (top + bottom) // 2
    l, r = 0, len(matrix[0]) - 1

    while l <= r:
        mid = (r + l) // 2
        if target > matrix[row][mid]:
            l = mid + 1
        elif target < matrix[row][mid]:
            r = mid - 1
        else:
            return True

    return False


def searchMatrix2(matrix: List[List[int]], target: int) -> bool:
    ROWS, COLS = len(matrix), len(matrix[0])
    top, bottom = 0, ROWS - 1

    while top <= bottom:
        row = (top + bottom) // 2
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bottom = row - 1
        else:
            break

    if not (top <= bottom):
        return False

    row = (top + bottom) // 2
    l, r = 0, COLS - 1

    while l <= r:
        m = (l + r) // 2
        if target > matrix[row][m]:
            l = m + 1
        elif target < matrix[row][m]:
            r = m - 1
        else:
            return True

    return False


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    for rows in matrix:
        l, r = 0, len(rows) - 1

        if target > rows[r]:
            continue

        while l <= r:
            mid = l + ((r - l) // 2)
            if target < rows[mid]:
                r = mid - 1
            elif target > rows[mid]:
                l = mid + 1
            else:
                return True

    return False


def searchMatrix4(matrix: List[List[int]], target: int) -> bool:
    merged_array = []

    for row in matrix:
        merged_array.extend(row)

    l, r = 0, len(merged_array) - 1

    while l <= r:
        m = l + ((r - l) // 2)

        if target > merged_array[m]:
            l = m + 1
        elif target < merged_array[m]:
            r = m - 1
        else:
            return True

    return False


if __name__ == '__main__':
    my_matrix = [[1, 3, 5, 7],
                 [10, 11, 16, 20],
                 [23, 30, 34, 60]]
    mat = [[1]]
    my_target = 60

    founded = searchMatrix(mat, my_target)
    print(founded)
