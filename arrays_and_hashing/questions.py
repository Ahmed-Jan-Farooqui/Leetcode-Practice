"""
    Top K Frequent Elements
    Given an integer array nums and an integer k, return the k most frequent elements within the array.

    The test cases are generated such that the answer is always unique.

    You may return the output in any order.
"""
from collections import defaultdict


def topKFrequent(nums, k):
    buckets = [[] for _ in range(len(nums) + 1)]
    hashmap = defaultdict(int)
    for num in nums:
        hashmap[num] += 1
    for key, value in hashmap.items():
        buckets[value].append(key)
    final = []
    while len(final) < k:
        for i in range(len(buckets) - 1, -1, -1):
            if len(final) == k:
                break
            if buckets[i]:
                for j in range(len(buckets[i])):
                    final.append(buckets[i][j])
                    if len(final) == k:
                        break
    return final


'''
    Products of Array Except Self

    Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

    Each product is guaranteed to fit in a 32-bit integer.

    Follow-up: Could you solve it in O(n)O(n) time without using the division operation?
'''


def productExceptSelf(nums):
    prefix = []
    suffix = []
    final = []

    for i in range(len(nums)):
        if not prefix:
            prefix.append(1)
            continue
        prefix.append(prefix[i-1] * nums[i-1])

    count = 0
    for i in range(len(nums) - 1, -1, -1):
        if not suffix:
            count += 1
            suffix.append(1)
            continue
        suffix.append(suffix[count-1] * nums[i+1])
        count += 1
    suffix.reverse()

    for i in range(len(nums)):
        final.append(prefix[i] * suffix[i])
    return final


'''
    Valid Sudoku

    You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

        Each row must contain the digits 1-9 without duplicates.
        Each column must contain the digits 1-9 without duplicates.
        Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.

    Return true if the Sudoku board is valid, otherwise return false

    Note: A board does not need to be full or be solvable to be valid.
'''


def validSudoku(board):
    # Declare variables
    hashmap_row = defaultdict(int)
    hashmap_col = defaultdict(int)
    hashmap_3x3 = defaultdict(int)

    # Check for rows
    for i in range(len(board[0])):
        for j in range(len(board[0])):
            if board[i][j] == ".":
                continue
            if hashmap_row[board[i][j]] == 1:
                print("Duplicate in rows")
                return False
            hashmap_row[board[i][j]] = 1
        hashmap_row = defaultdict(int)

    # Check for columns
    for i in range(len(board[0])):
        for j in range(len(board[0])):
            if board[j][i] == ".":
                continue
            if hashmap_col[board[j][i]] == 1:
                return False
            hashmap_col[board[j][i]] = 1
        hashmap_col = defaultdict(int)

    # Check for 3x3 sub-boxes
    # First loop steps through the rows at a step of 3
    for i in range(0, len(board[0]), 3):
        # Second loop steps through the columns at a step of 3
        for j in range(0, len(board[0]), 3):
            # Third loop steps through the 3x3 sub-box
            for k in range(3):
                for l in range(3):
                    if board[i+k][j+l] == ".":
                        continue
                    print(f"3x3 {j}: {board[i+k][j+l]}")
                    if hashmap_3x3[board[i+k][j+l]] == 1:
                        print("Duplicate in 3x3")
                        return False
                    hashmap_3x3[board[i+k][j+l]] = 1
            hashmap_3x3 = defaultdict(int)

    return True
