class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]

        left, right = 0, len(nums) - 1 

        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= nums[0]:
                left = mid +1 
            else: right = mid 
        return nums[left] 
    
    
    # def position_of_max(self,nums):
    #     m = nums[0]
    #     position = 0
    #     for index, value in enumerate(nums):
    #         if value > m:
    #             m = value
    #             position = index
    #     return position

    # def findMin(self, nums: List[int]) -> int:
    #     # find position of maximum value 
    #     # put it in k 
    #     # reverse rotate k number of times '
    #     # return first element - min

    #     if nums[0] <= nums[-1]:
    #         return nums[0]
    
    #     k = self.position_of_max(nums) 
        
    #     for _ in range(k+1) :
    #         last_value = nums[0]
    #         for j in range(1,len(nums)):
    #             nums[j - 1] = nums[j]
    #         nums[-1] = last_value
    #     return nums[0]
            

            
        