class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        buy = prices[0]
        for i in range(1,len(prices)):
            sell = prices[i]
            if sell < buy:
                buy = sell
            maxProf = max(maxProf, sell - buy)
        return maxProf