class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res= set()
        count = {}
        max_count = len(nums)//3
        for num in nums:
            count[num] = count.get(num,0) + 1 

        for c in count:
            if count[c] > max_count:
                res.add(c)
        return list(res)