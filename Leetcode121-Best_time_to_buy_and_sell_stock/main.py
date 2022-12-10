# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# ====================================================

prices = [7,1,5,3,6,4]

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        l = 0
        r = 1
        profit = 0
        max_profit = 0
        while r<len(prices):

            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
            

            if prices[r] < prices[l]:
                l = r
                r = l+1
            else:
                r += 1
                
        return max_profit 
        
sol = Solution()
r = sol.maxProfit(prices)


print(f'Output : {r}')



