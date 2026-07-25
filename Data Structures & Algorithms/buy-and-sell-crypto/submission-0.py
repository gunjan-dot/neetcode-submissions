class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_return = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] - prices[i] > max_return:
                    max_return = prices[j] - prices[i]
        return max_return