class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if target - nums[j] == nums[i] :
        #             return [i,j]
        seen ={}
        for i, num in enumerate(nums):
            required = target - num
            if required in seen:
                return [seen[required],i]
            seen[num] = i
