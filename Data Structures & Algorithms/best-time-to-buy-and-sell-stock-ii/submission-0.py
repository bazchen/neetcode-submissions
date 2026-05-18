class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    # Solution: Greedy - O(n)
        # Track profit
        profit = 0

        # Loop thru prices (skipping first day)
        for i in range(1, len(prices)):
            # If current price is higher than prev day price, then profit
            diff = prices[i] - prices[i-1]
            if diff > 0:
                profit += diff

        # return total profit
        return profit
        