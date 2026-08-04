class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value=prices[0]
        ans=0
        for i in range(1, len(prices)):
            ans=max(ans, prices[i]-min_value)

            min_value=min(min_value, prices[i])

        return ans