class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxpro = 0
        l = 0
        
        for r in range(len(prices)):
            if prices[l] > prices[r]:
               
                l = r
            else:
                maxpro = max(maxpro , prices[r] - prices[l])
            
        return maxpro
        
