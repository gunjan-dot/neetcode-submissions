class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float("inf")
        for i in range(len(nums)):
            s = 0
            for j in range(i,len(nums)):
                s += nums[j] 
                if s >= target:
                    min_len = min(j-i+1, min_len)
                    break
        return 0 if  min_len == float("inf") else min_len