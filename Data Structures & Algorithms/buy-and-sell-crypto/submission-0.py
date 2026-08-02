class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0


        for currentPrice in prices:
            minPrice  = min(minPrice, currentPrice)
            currentProfit = currentPrice  - minPrice
            maxProfit = max(maxProfit,currentProfit)


        return maxProfit