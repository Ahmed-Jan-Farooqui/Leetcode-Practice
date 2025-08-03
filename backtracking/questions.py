def subsets(self, nums: List[int]) -> List[List[int]]:
    final = []
    def _backTrackSubSets(subset, idx, nums):
        nonlocal final
        if idx >= len(nums):
            final.append(subset)
            return
        # Add this idx
        subset_without = list(subset)
        subset.append(nums[idx])
        subset_with = list(subset)
        _backTrackSubSets(subset_with, idx+1, nums)
        # Don't add this idx
        _backTrackSubSets(subset_without, idx+1, nums)
    _backTrackSubSets([], 0, nums)
    return final