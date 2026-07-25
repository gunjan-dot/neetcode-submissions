class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        k %= n
        temp = [0]* n

        for i in range(n):
            temp[(i+k) % n] = nums[i]

        nums[:] = temp

        # k %= len(nums) 
        # while k:
        #     last= nums[-1]
        #     for j in range(len(nums)-1, 0 , -1):
        #         nums[j] = nums[j-1]
        #     nums[0] = last 
        #     k-=1


        # for i in range(k):
        #     last = nums[-1]
        #     for j in range(len(nums)-1, 0 , -1):
        #         nums[j] = nums[j-1]
        #     nums[0] = last 