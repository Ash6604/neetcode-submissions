class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxpro = 0
        minprice = float('inf')
        for i in range(len(prices)):
            minprice = min(minprice , prices[i])
            maxpro = max(maxpro , prices[i]-minprice)
        return maxpro
        