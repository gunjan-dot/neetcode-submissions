class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0 
        store = set(nums)

        for num in nums:
            curr = num
            streak = 0 
            while curr in store:
                curr += 1
                streak += 1
            max_len = max(max_len, streak)
        return max_len
        


