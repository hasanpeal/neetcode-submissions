class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        start = 0
        length = len(prices)

        for end in range(start+1, length, 1):
            profit = prices[end] - prices[start]
            if profit > 0:
                maxProfit = max(maxProfit, profit)
            else:
                start = end
        
        return maxProfit

        