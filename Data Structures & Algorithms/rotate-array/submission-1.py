class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums) 
        while k:
            last= nums[-1]
            for j in range(len(nums)-1, 0 , -1):
                nums[j] = nums[j-1]
            nums[0] = last 
            k-=1
        # for i in range(k):
        #     last = nums[-1]
        #     for j in range(len(nums)-1, 0 , -1):
        #         nums[j] = nums[j-1]
        #     nums[0] = last 