class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1

        #by closing in from side, we automatically prioritize the width

        maxVal = float('-inf')

        while l < r:
            area = (min(heights[l], heights[r])) * (r-l) #area
            maxVal = max(maxVal, area)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return maxVal