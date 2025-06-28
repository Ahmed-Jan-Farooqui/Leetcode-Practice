'''
Longest Substring Without Repeating Characters


Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.
'''
def lengthOfLongestSubstring(s: str) -> int:
    if len(s) < 2:
        return len(s)
    hashmap = {}
    l = 0
    r = 0
    max_count = 1
    while l <= r and r != len(s):
        # Right most letter is a duplicate.
        while hashmap.get(s[r]) is not None:
            # Shrink window till duplicate removed.
            hashmap.pop(s[l], None)
            l += 1
        # If right most letter not a duplicate, add.
        hashmap[s[r]] = 1
        max_count = max(max_count, r - l + 1)
        r += 1
    return max_count