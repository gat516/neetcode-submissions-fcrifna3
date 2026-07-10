class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        max_profit = 0

        for i in range(0, len(prices) - 1):
            #we have a profit
            if prices[r] >= prices[l]:
                profit = prices[r] - prices[l]
                print(profit)
                max_profit = max(profit, max_profit)
                r += 1
    
            else: # no profit
                print("no profit: ", l, " ", r, " ", prices[r] - prices[l])
                l = r
                r += 1

        return max_profit