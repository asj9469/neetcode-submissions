class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # try iterating through the whole array and then for each,
        # we try to expand as much as possible

        maxArea = max(heights)
        for i in range(len(heights)):
            l, r = i, i

            while l >= 0 and heights[l] >= heights[i]:
                l -=1
            
            while r < len(heights) and heights[r] >= heights[i]:
                r += 1
            
            # min height is the current height at this point
            maxArea = max(maxArea, (r-l-1) * heights[i])

        return maxArea