class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val, max_diff = float('inf'), float('-inf')

        for i, p in enumerate(prices):
            min_val = min(min_val, p) # update minimum value right away
            max_diff = max(max_diff, p - min_val)

        return max_diff if max_diff != float('-inf') else 0
