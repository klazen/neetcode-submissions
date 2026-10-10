class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        n=len(prices)
        if n<2:
            return 0
        if n==2 and prices[1]<=prices[0]:
            return 0
        left=prices.index(min(prices[:n-1]))
        right=n-1-prices[::-1].index(max(prices[1:]))
        if left<=right:
            return prices[right]-prices[left]
        else:
            return max(max(prices[left+1:])-prices[left],prices[right]-min(prices[:right]),0)