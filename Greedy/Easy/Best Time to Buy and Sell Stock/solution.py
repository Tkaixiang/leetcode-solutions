class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1. Iterate throuh prices, and update the minimum price as you go
        # 2. Calculate the maximum profit earned based on that minimum price
        # =====
        # Why do you not need to care about finding the lowest price first?
        # A lower minimum price can be updated later on as we can only sell 
        # AFTER BUYING, so finding the current "best profit" in the given minimum price window
        # is more efficient (a minimum price window ends when we hit a new minimum price)
        
        highestProfit = 0
        lowest = 9999999999999999999
        for x in range(0, len(prices), 1):
            # New minimum price window started
            if (prices[x] < lowest):
                lowest = prices[x]
            else: # Calculate profit in that min price window
                profit = prices[x] - lowest
                if (profit > highestProfit):
                    highestProfit = profit
                
        
        return highestProfit
    
        # [7,2,8,3,1,4]