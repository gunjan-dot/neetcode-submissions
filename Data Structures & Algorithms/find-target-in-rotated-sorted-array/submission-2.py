class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2 
            if nums[mid]  > nums[right]:
                left = mid + 1 
            else:
                right = mid 

        pivot = left 

        def binary_search(l:int, r:int) -> int:
            while l <=r:
                m = (l+r) // 2 
                if nums[m] == target:
                    return m 
                elif nums[m] > target:
                    r = m - 1 
                else:
                    l = m + 1 
            return -1 

        result = binary_search(0, pivot)
        if result != -1:
            return result 
        
        return binary_search(pivot, len(nums) -1)


