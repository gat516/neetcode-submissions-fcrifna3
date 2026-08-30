class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        l, r = 0, 1
        maximum_profit = 0

        while r < len(prices):  
            #profit
            if prices[l] <= prices[r]:
                profit = prices[r] - prices[l]
                maximum_profit = max(profit,maximum_profit)
                r += 1
                print("profit: ", profit, " | ", l, ":", r )
                #no profit
            elif prices[l] > prices[r]:
                print("no profit | ", l, ":", r)
                l += 1

        return maximum_profit



            #no profit