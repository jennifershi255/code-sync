class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        res = 0

        for right in range(len(prices)):

            while prices[left] > prices[right]:
                left += 1
            
            profit = prices[right] - prices[left]
            res = max(res, profit)
        
        return res