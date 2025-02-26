"""Top K Frequent Elements
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


print(productExceptSelf([1, 2, 4, 6]))
