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

'''
    Longest Repeating Character Replacement

    You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

    After performing at most k replacements, return the length of the longest substring which contains only one distinct character.
'''

def characterReplacement(s: str, k: int) -> int:
    if len(s) < 2:
        return len(s)
    from collections import defaultdict
    counts = defaultdict(int)
    most_freq_letter = s[0]
    max_count = 0
    # Helper function
    def getMostFrequentLetter():
        max_f_l = ""
        max_f = 0
        for key in counts.keys():
            if max_f < counts[key]:
                    max_f_l = key
                    max_f = counts[key]
        return max_f_l
    l = 0
    r = 0
    while l <= r and r < len(s):
        counts[s[r]] += 1
        most_freq_letter = getMostFrequentLetter()
        # Is window valid?
        if r - l + 1 - counts[most_freq_letter] <= k:
            max_count = max(r - l + 1, max_count)
        # If not valid, shrink till it is.
        else:
            while r - l + 1 - counts[most_freq_letter] > k:
                counts[s[l]] -= 1
                l += 1
                most_freq_letter = getMostFrequentLetter()
        r += 1
    return max_count


'''
    Permutation in String

    You are given two strings s1 and s2.

    Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

    Both strings only contain lowercase letters.
'''
def checkInclusion(self, s1: str, s2: str) -> bool:
    '''
        If the letters in s1 are present in s2 with the same counts,
        then we have a permutation.
    '''
    # O ( 26 * n ) solution
    # if len(s1) > len(s2):
    #     return False
    # from collections import defaultdict
    # counts_s1 = defaultdict(int)
    # counts_s2 = defaultdict(int)
    # # O(n)
    # for letter in s1:
    #     counts_s1[letter] += 1
    # l = 0
    # r = len(s1) - 1
    # # O(n)
    # for letter in s2[l:r+1]:
    #     counts_s2[letter] += 1
    # def isEqual():
    #     for key in counts_s1.keys():
    #         if counts_s2.get(key) != counts_s1[key]:
    #             return False
    #     return True
    # # O(n)
    # while l <= r and r != len(s2):
    #     # Check if equal
    #     if isEqual(): # O(26)
    #         return True
    #     else:
    #         # Move window forward.
    #         counts_s2[s2[l]] -= 1 
    #         l += 1
    #         r += 1
    #         if r == len(s2):
    #             break
    #         counts_s2[s2[r]] += 1 
    # return False


    # O(n) solution
    '''
        If the letters in s1 are present in s2 with the same counts,
        then we have a permutation.
        This is a more efficient solution where we will keep track of the matches so far.
        Will only have to loop once this way, and can update as we update the window phir.
    '''
    if len(s1) > len(s2):
        return False
    from collections import defaultdict
    counts_s1 = defaultdict(int)
    counts_s2 = defaultdict(int)
    matches = 0
    for letter in s1:
        counts_s1[letter] += 1
    l = 0
    r = len(s1) - 1
    for letter in s2[l:r+1]:
        counts_s2[letter] += 1
        if counts_s1.get(letter) == counts_s2[letter]:
            matches += 1
    while l <= r and r != len(s2):
        # Check if equal
        if matches == len(counts_s1.keys()):
            return True
        else:
            # Move window forward.
            # Remove match if the current letter was contributing to one.
            if counts_s1.get(s2[l]) == counts_s2[s2[l]]:
                matches -= 1
            counts_s2[s2[l]] -= 1 
            l += 1
            r += 1
            if r == len(s2):
                break
            # Add match if newly added letter forms a matcb
            counts_s2[s2[r]] += 1 
            if counts_s1.get(s2[r]) == counts_s2[s2[r]]:
                matches += 1
    return False
            



            
