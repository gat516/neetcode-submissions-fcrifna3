class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestProfit = 0
        buy, sell = 0, 1


        while sell < len(prices):
            if  prices[buy] > prices[sell]:
                buy = sell
                print("moving buy to sell")
            else:
                profit = prices[sell] - prices[buy]
                print(buy, " ", sell, " profit: ", profit)
                bestProfit = max(profit, bestProfit)
            sell += 1
        return bestProfit
