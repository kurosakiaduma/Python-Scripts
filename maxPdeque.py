from collections import dequeue

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        self.min_day = prices.index(min(prices))
        self.max_day = prices.index(max(prices))
        
        while self.max_day == 0:
            prices.pop(0)
            
            
        
            
        