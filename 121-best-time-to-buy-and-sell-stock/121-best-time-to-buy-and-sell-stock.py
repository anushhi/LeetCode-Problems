class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = float('inf')
        ans = 0
        for sell in prices:
            if sell < buy:
                buy = sell
                
            else:
                profit = sell-buy
                ans = max(ans,profit)
                
        return ans
                
            
            