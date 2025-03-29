'''
    Two Integer Sum II

    Given an array of integers numbers that is sorted in non-decreasing order.

    Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

    There will always be exactly one valid solution.

    Your solution must use O(1)O(1) additional space.
'''


def twoSum(numbers: list[int], target):
    # # O(n) space solution
    # hash_difference = {target - numbers[i]: (numbers[i], i)
    #                    for i in range(0, len(numbers))}
    # for i in range(len(numbers)):
    #     value = hash_difference.get(numbers[i])
    #     if not value:
    #         continue
    #     if value[1] > i:
    #         return [i+1, value[1]+1]
    # O(1) space solution. Use the fact that the array is sorted. Pretty simple.
    l = 0
    r = len(numbers) - 1
    while l < r:
        value = numbers[l] + numbers[r]
        if value < target:
            l += 1
        elif value > target:
            r -= 1
        elif value == target:
            return [l+1, r+1]


'''
    3Sum

    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

    The output should not contain any duplicate triplets. You may return the output and the triplets in any order.
'''


def threeSum(nums: list[int]):
    '''
        Need to select three numbers, so we iterate over the array for the first number, and select the 
        two other numbers via TwoSum. O(n * n) = O(n^2)
    '''
    l = 1
    r = len(nums) - 1
    final = []
    nums.sort()
    for i in range(len(nums)):
        l = i+1
        r = len(nums) - 1
        if i != 0 and nums[i-1] == nums[i]:
            continue
        while l < r:
            if l != i+1 and nums[l-1] == nums[l]:
                l += 1
                continue
            if r != len(nums) - 1 and nums[r+1] == nums[r]:
                r -= 1
                continue
            sum = nums[i] + nums[l] + nums[r]
            if sum == 0:
                final.append([nums[i], nums[l], nums[r]])
                l += 1
            elif sum > 0:
                r -= 1
            elif sum < 0:
                l += 1
    return final


'''
Container With Most Water

You are given an integer array heights where heights[i] represents the height of the ithith bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.
'''


def maxArea(heights: list[int]):
    '''
        Use left and right pointers, and track maximum value. Move the pointer that is the limiter/min.
    '''
    max = -10000
    l = 0
    r = len(heights) - 1
    while l < r:
        height = min(heights[l], heights[r])
        width = r - l
        area = height * width
        if max < area:
            max = area
        # Which ptr do I move?
        if height == heights[l]:
            l += 1
        else:
            r -= 1
    return max


'''
Trapping Rain Water

You are given an array non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.
'''


def trapRainWater(height: list[int]):
    max_left = []
    max_right = []
    max_l = 0
    max_r = 0
    total = 0
    for i in range(len(height)):
        rightward_idx = len(height) - (i + 1)
        max_left.append(max_l)
        max_right.append(max_r)
        if height[i] > max_l:
            max_l = height[i]
        if height[rightward_idx] > max_r:
            max_r = height[rightward_idx]

    max_right.reverse()
    for i in range(len(height)):
        minimum = min(max_left[i], max_right[i])
        # print(minimum)
        value = minimum - height[i]
        if value > 0:
            total += value
    return total
