class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 
        max_profit = 0 
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r 
            r = r + 1 

        return max_profit 
        # max_return = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         if prices[j] - prices[i] > max_return:
        #             max_return = prices[j] - prices[i]
        # return max_return