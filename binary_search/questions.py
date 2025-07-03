def search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m - 1
        else:
            return m
    return -1
        


'''
Search a 2D Matrix

You are given an m x n 2-D integer array matrix and an integer target.

    Each row in matrix is sorted in non-decreasing order.
    The first integer of every row is greater than the last integer of the previous row.

Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?
'''
def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    '''
        1. Find correct row using binary search.
        2. Find correct number using binary search.
    '''
    # Find correct row.
    l_row, r_row = 0, len(matrix) - 1
    critical_row = -1
    while l_row <= r_row:
        m_row = (l_row + r_row) // 2
        # Check if number is in bounds of this row.
        if target <= matrix[m_row][-1] and target >= matrix[m_row][0]:
            critical_row = m_row
            break
        # Check if smallest number of this row less than target.
        elif target < matrix[m_row][0]:
            r_row = m_row - 1
        # Check if largest number of this row is less than target.
        elif target > matrix[m_row][-1]:
            l_row = m_row + 1
    # Exit early if even the row not found.
    if critical_row == -1:
        return False    
    # Now run binary search on the critical row.
    l, r = 0, len(matrix[critical_row]) - 1
    while l <= r:
        m = (l+r) // 2
        if target > matrix[critical_row][m]:
            l = m+1
        elif target < matrix[critical_row][m]:
            r = m-1
        else:
            return True
    return False



'''
Koko Eating Bananas

You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents the number of hours you have to eat all the bananas.

You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.

Return the minimum integer k such that you can eat all the bananas within h hours.
'''
def minEatingSpeed(piles: list[int], h: int) -> int:
    '''
    1. I start my eating rate from half the value of the max.
    2. I eat banans at that rate.
        a. If I have eaten the banans in less than h time, I will move
        the right bound towards the value one less than my current rate.
        I will also store this current rate as a solution.
        b. If it takes me longer than h time to eat the bananas, then
        I will move the left bound towards the value one more than
        my current rate.
    3. Continue until both left and right endpoints the same.
    '''
    from math import ceil
    l, r = 1, max(piles)
    val = -1
    while l <= r:
        k = ceil((l+r) / 2)
        total = 0
        # Check how long it takes me to eat the bananas.
        for pile in piles:
            total += ceil(pile / k)
        # If my total is < h, I can try decreasing my eating rate.
        if total <= h:
            val = k
            r = k-1
        # If my total is > h, then I know I must increase my eating rate.
        elif total > h:
            l = k+1 
    return val


'''
Find Minimum in Rotated Sorted Array
Solved

You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

    [3,4,5,6,1,2] if it was rotated 4 times.
    [1,2,3,4,5,6] if it was rotated 6 times.

Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.

Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?
'''
def findMin(nums: list[int]) -> int:
    '''
    I will do this:
    1. Check if the middle number is greater than the right most number.
        a. If it is, then that means the sorting has been violated towards
        the right side of the array.
        b. If it isn't, then that means the sorting violation lies on the
        left side of the array.
    '''
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l+r) // 2
        if nums[m] > nums[r]:
            l = m+1
        elif nums[m] < nums[r]:
            r = m
        else:
            return nums[m]
    return nums[0]


'''
Search in Rotated Sorted Array

You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

    [3,4,5,6,1,2] if it was rotated 4 times.
    [1,2,3,4,5,6] if it was rotated 6 times.

Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.

You may assume all elements in the sorted rotated array nums are unique,

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?
'''
def search(nums: list[int], target: int) -> int:
    '''
    We want to do the following:
    1. I want to find the inflection point, and then search both arrays
    using binary search.
    2. To find the inflection point, I can:
        a. Check to see if the mid value is less than the right most number.
            i. If it is, then that means the numbers to my right are sorted (since no duplicates), so I can move left.
            ii. If it isn't, then that means the second sorted array is somewhere to the right of the mid point.
    3. Once the inflection point is found, the problem is trivial.
    4. This will be 3*logn as I do three logn operations.
    '''
    l, r = 0, len(nums) - 1
    inflection_point = -1
    while l <= r:
        m = (l+r) // 2
        if nums[m] > nums[r]:
            l = m+1
        elif nums[m] < nums[r]:
            r = m
        else:
            inflection_point = m
            break
    
    if inflection_point == -1:
        inflection_point = 0
    print(inflection_point)
    l_one, r_one = inflection_point, len(nums) - 1
    l_two, r_two = 0, inflection_point-1
    
    while l_one <= r_one:
        m = (l_one + r_one) // 2
        if target < nums[m]:
            r_one = m-1
        elif target > nums[m]:
            l_one = m+1
        else:
            return m
    
    while l_two <= r_two:
        m = (l_two + r_two) // 2
        print(l_two, r_two, m)
        if target < nums[m]:
            r_two = m-1
        elif target > nums[m]:
            l_two = m+1
        else:
            return m
    
    return -1


'''
Time Based Key-Value Store

Implement a time-based key-value data structure that supports:

    Storing multiple values for the same key at specified time stamps
    Retrieving the key's value at a specified timestamp

Implement the TimeMap class:

    TimeMap() Initializes the object.
    void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
    String get(String key, int timestamp) Returns the most recent value of key if set was previously called on it and the most recent timestamp for that key prev_timestamp is less than or equal to the given timestamp (prev_timestamp <= timestamp). If there are no values, it returns "".

Note: For all calls to set, the timestamps are in strictly increasing order.
'''

class TimeMap:
    from collections import defaultdict
    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))
        return None

    def get(self, key: str, timestamp: int) -> str:
        '''
        Check if timestamp exists using binary search.
        If timestamp doesn't exist, I use binary search to find the next best value. 
        Here, the basic idea is:
            1. If the target timestamp is less than the timestamp I am looking at currently,
            then that means I don't need to consider all values to the right of this timestamp (inclusive).
            2. If the target timestamp is greater than the timestamp I am looking at currently,
            then that means this is a possible value. It also means I don't need to consider the
            values to the left of this value (inclusive) as they are guaranteed to be smaller than
            this timestamp, so we don't care about them. 
        '''
        time_map_arr = self.time_map[key]
        # print(time_map_arr)
        if time_map_arr == []:
            return ""
        l, r = 0, len(time_map_arr) - 1
        while l <= r:
            m = (l+r) // 2
            if timestamp < time_map_arr[m][1]:
                r = m-1
            elif timestamp > time_map_arr[m][1]:
                l = m+1
            else:
                return time_map_arr[m][0]
        # I don't find the value, so i must look for the largest value
        # less than target.
        l, r = 0, len(time_map_arr) - 1
        next_best_value = -1
        while l <= r:
            m = (l + r) // 2
            if timestamp < time_map_arr[m][1]:
                r = m - 1
            else:
                next_best_value = m
                l = m+1
        return time_map_arr[next_best_value][0] if time_map_arr[next_best_value][1] < timestamp else ""
                




